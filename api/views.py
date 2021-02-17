from rest_framework.generics import ListAPIView, RetrieveAPIView

from shop.models import Product
from .serializers import ProductSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
