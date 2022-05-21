from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = (
            'id',
            'prod_name',
            'prod_desc',
            'prod_price',
            'prod_imgname',
            'prod_imgsrc',
            'prodcat',
            'vend',
        )
