from django.urls import path
from django.views.generic import RedirectView

from .views import product_category_list_view, product_vendor_list_view, ProductDetailView, order_view


urlpatterns = [
    path('', RedirectView.as_view(url='product_category_list/', permanent=True)),
    path('product_category_list/',   product_category_list_view,  name='product_category_list'),
    path('product_vendor_list/',     product_vendor_list_view,    name='product_vendor_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('order/',                   order_view,                  name='order'),
]
