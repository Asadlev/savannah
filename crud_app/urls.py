from django.urls import path
from . import views
from .views import ( ProductDeleteView,
ProductDetailView, ProductUpdateView,
)


app_name = 'crud_app'

urlpatterns = [
    # path('create', ProductCreateView.as_view(), name='create_product'),
    path('delete/<slug:product_slug>/', ProductDeleteView.as_view(), name='delete_product'),
    path('update/<slug:product_slug>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='detail_product'),
]
