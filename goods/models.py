from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Category(models.Model):
    # CHOICE_CATEGORY = [
    #     ('спорт', 'Спорт'),
    #     ('электроника', 'Электроника'),
    #     ('бытовая техника', 'Бытовая техника'),
    #     ('обувь', 'Обувь'),
    #     ('детям', 'Детям'),
    #     ('дом', 'Дом')
    # ]
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание товара')
    image = models.ImageField(upload_to='product_images/', null=False, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Кол-во товара(Сколько штук)')
    stock = models.BooleanField(default=False, verbose_name='Акция имеется')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка в %')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.stock and self.discount <= 0:
            raise ValidationError('Если акция имеется, то скидка должен быть больше нуля 0.')

    def __str__(self):
        return f'{self.name} Цена - {self.price}'

    def get_absolute_url(self):
        return reverse('crud_app:detail_product', args=[str(self.slug)])

    # Пишем функцию для отображения 000id
    def display_id(self):
        return f'{self.id:04}'

    # Делаем расчет для скидки
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price

    def __str__(self):
        return self.name


class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Товар: {self.product.name}'




