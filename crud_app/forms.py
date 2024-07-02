from django import forms
from goods.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'name',
            'description',
            'quantity',
            'price',
            'stock',
            'discount',
            'category',

            'image'
        ]




