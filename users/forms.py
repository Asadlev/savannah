from django import forms

from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        ]






