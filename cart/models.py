from django.db import models
from users.models import User
from goods.models import Product


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_cart', verbose_name='Пользователь')
    session_key = models.CharField(max_length=40, blank=True, null=True, verbose_name='Временная регистрация')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = CartQuerySet.as_manager()

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.user.username if self.user else "анонимный"} | Товар {self.product.name} | Кол-во {self.quantity}'
