from django.urls import path
from django.views.generic import RedirectView

from .views import ProductList, ProductDetail


urlpatterns = [
    path('',                  RedirectView.as_view(url='products', permanent=True)),
    path('products',          ProductList.as_view(), name='product_list_api'),
    path('products/<int:pk>', ProductDetail.as_view()),
]
