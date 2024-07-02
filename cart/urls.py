from django.urls import path
from .views import cart_add, cart_change, cart_delete, thanks

app_name = 'cart'

urlpatterns = [
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart_change/<int:product_id>/', cart_change, name='cart_change'),
    path('cart_delete/<int:cart_id>/', cart_delete, name='cart_delete'),
    path('thanks/', thanks, name='thanks'),
]
