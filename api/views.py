from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from shop.models import Product

from .permissions import IsSuperuserOrReadOnly
from .serializers import ProductSerializer


class ProductsAPIView(ListCreateAPIView):

    permission_classes = (IsSuperuserOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsSuperuserOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
