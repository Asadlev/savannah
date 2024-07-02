from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    login,
    logout,
    register,
    profile,
    user_cart,
)

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('user_cart/', user_cart, name='user_cart'),
]




