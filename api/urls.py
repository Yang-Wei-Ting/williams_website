from django.urls import path

from .views import ListProduct, DetailProduct


urlpatterns = [
    path('products',          ListProduct.as_view()),
    path('products/<int:pk>', DetailProduct.as_view()),
]
