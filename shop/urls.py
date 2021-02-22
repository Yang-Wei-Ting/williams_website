from django.urls import path
from django.views.generic import RedirectView

from .views import (
    product_category_list_view,
    product_vendor_list_view,
    product_detail_view,
)


urlpatterns = [
    path('',          RedirectView.as_view(url='products/browse-by-category/', permanent=True)),
    path('products/', RedirectView.as_view(url='browse-by-category/', permanent=True)),
    path('products/browse-by-category/', product_category_list_view, name='product_category_list'),
    path('products/browse-by-vendor/',   product_vendor_list_view,   name='product_vendor_list'),
    path('products/<int:pk>/',           product_detail_view,        name='product_detail'),
]
