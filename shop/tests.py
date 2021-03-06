from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import (
    ProductCategory,
    Vendor,
    Product,
    Order,
)


class ShopModelsTest(TestCase):
    def setUp(self):
        self.prodcat = ProductCategory.objects.create(
            prodcat_name="prodcat_name",
        )
        self.vend = Vendor.objects.create(
            vend_name="vend_name",
            vend_country="TW",
            vend_city="vend_city",
        )
        self.prod = Product.objects.create(
            prod_name="prod_name",
            prod_desc="prod_desc",
            prod_price=3.14,
            prod_imgname="prod_imgname",
            prod_imgsrc="prod_imgsrc",
            prodcat=self.prodcat,
            vend=self.vend,
        )
        self.user=get_user_model().objects.create_user(
            username="username",
            password="password",
        )
        self.order = Order.objects.create(
            cust=self.user,
            prod=self.prod,
            order_quantity=99,
            order_totalprice=99 * self.prod.prod_price,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.prodcat), self.prodcat.prodcat_name)
        self.assertEqual(str(self.vend), self.vend.vend_name)
        self.assertEqual(str(self.prod), self.prod.prod_name)
        self.assertEqual(str(self.order), f"Order ID {self.order.id}")

    def test_get_absolute_url(self):
        self.assertEqual(self.prod.get_absolute_url(), "/shop/products/1/")
