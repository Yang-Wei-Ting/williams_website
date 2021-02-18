from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shop.models import Product
from .serializers import ProductSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
