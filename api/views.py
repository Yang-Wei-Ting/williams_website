from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from shop.models import Product
from .permissions import IsSuperuserOrReadOnly
from .serializers import ProductSerializer


class ProductList(ListCreateAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperuserOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
