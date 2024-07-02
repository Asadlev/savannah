from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from cart.models import Cart
from goods.models import Product


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart.quantity += 1
        cart.save()
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, product=product)
        cart.quantity += 1
        cart.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))


def cart_change(request, product_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        product = get_object_or_404(Product, id=product_id)
        if request.user.is_authenticated:
            cart_item = get_object_or_404(Cart, user=request.user, product=product)
        else:
            session_key = request.session.session_key
            if session_key:
                cart_item = get_object_or_404(Cart, session_key=session_key, product=product)
            else:
                return JsonResponse({'error': 'Session not found'}, status=400)

        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()
        return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.products_price()})

    return redirect(request.META.get('HTTP_REFERER', 'home'))


def cart_delete(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, user=request.user, id=cart_id)
    else:
        session_key = request.session.session_key
        if session_key:
            cart_item = get_object_or_404(Cart, session_key=session_key, id=cart_id)
        else:
            return JsonResponse({'error': 'Session not found'}, status=400)

    cart_item.delete()
    messages.success(request, "Товар удален из корзины.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def thanks(request):
    context = {
        'title': 'savannah - thanks'
    }
    return render(request, 'cart/thankyou.html', context)
