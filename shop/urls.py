from django.urls import path
from django.views.generic import RedirectView

from .views import (
    ProductCategoriesView,
    ProductCategoryProductsView,
    VendorsView,
    VendorProductsView,
    ProductsView,
    product_view,
)


urlpatterns = [
    path('',                             RedirectView.as_view(url='products/', permanent=True)),
    path('product-categories/<int:pk>/', RedirectView.as_view(url='products/', permanent=True)),
    path('vendors/<int:pk>/',            RedirectView.as_view(url='products/', permanent=True)),

    path('product-categories/',                   ProductCategoriesView.as_view(),       name='product_categories'),
    path('product-categories/<int:pk>/products/', ProductCategoryProductsView.as_view(), name='product_category_products'),
    path('vendors/',                              VendorsView.as_view(),                 name='vendors'),
    path('vendors/<int:pk>/products/',            VendorProductsView.as_view(),          name='vendor_products'),
    path('products/',                             ProductsView.as_view(),                name='products'),
    path('products/<int:pk>/',                    product_view,                          name='product'),
]
