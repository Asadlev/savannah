from django_filters import FilterSet, CharFilter
from goods.models import Product, Category
from django import forms

'''
Создаем свой набор фильтров для модели Product.
FilterSet, который мы наследуем,
должен чем-то напомнить знакомые вам Django-generic 
'''


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            # поиск по названию
            'name': ['icontains'],
        }



