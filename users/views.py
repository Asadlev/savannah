from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from goods.models import Category
from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from .models import User
from django.contrib import auth, messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем форму и получаем объект пользователя
            messages.success(request, 'Успешная регистрация и вход.')
            auth.login(request, user)  # Логиним пользователя
            return redirect(reverse('goods:catalogs'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }

    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы вошли в аккаунт.')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('goods:catalogs'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'savannah - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    messages.success(request, 'Вы вышли из аккаунта.')
    auth.logout(request)
    return redirect('goods:catalogs')


@login_required
def profile(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен.')
            return redirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Профиль',
        'form': form,
        'categories': categories,
    }

    return render(request, 'users/profile.html', context)


# Cart
def user_cart(request):
    return render(request, 'users/cart.html')





