from rest_framework.generics import ListAPIView, RetrieveAPIView

from shop.models import Product
from .serializers import ProductSerializer


class ListProduct(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
