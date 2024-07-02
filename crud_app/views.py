from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .forms import ProductForm
from goods.models import Product


# Product - views
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'crud_app/detail_product.html'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


# class ProductsCreateView(CreateView):
#     model = Products
#     form_class = ProductForm
#     template_name = 'crud_app/create_product.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'crud_app/update_product.html'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'crud_app/delete_product.html'
    success_url = reverse_lazy('goods:catalogs')
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'








