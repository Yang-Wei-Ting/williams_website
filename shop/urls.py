from django.urls import path
from django.views.generic import RedirectView

from .views import product_list_view, product_detail_view


urlpatterns = [
    path('',          RedirectView.as_view(url='products/browse-by-category/', permanent=True)),
    path('products/', RedirectView.as_view(url='browse-by-category/',          permanent=True)),
    path('products/browse-by-category/', product_list_view,   kwargs={'browse_by': 'Category'}, name='product_category_list'),
    path('products/browse-by-vendor/',   product_list_view,   kwargs={'browse_by': 'Vendor'},   name='product_vendor_list'),
    path('products/<int:pk>/',           product_detail_view,                                   name='product_detail'),
]
