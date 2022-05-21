from django.urls import path
from django.views.generic import RedirectView

from .views import ProductAPIView, ProductsAPIView

urlpatterns = [
    path('',                  RedirectView.as_view(url='products', permanent=True)),

    path('products',          ProductsAPIView.as_view(), name='products_api'),
    path('products/<int:pk>', ProductAPIView.as_view(),  name='product_api'),
]
