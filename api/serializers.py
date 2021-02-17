from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('prod_name', 'prod_desc', 'prod_price', 'prod_imgname', 'prod_imgsrc', 'prodcat_id', 'vend_id')
