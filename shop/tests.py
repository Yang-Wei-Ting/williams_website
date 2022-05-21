from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import (
    ProductCategory,
    Vendor,
    Product,
    Order,
)


class ShopTest(TestCase):
    # models
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
            prod_imgname="hamburger.jpg",
            prod_imgsrc="prod_imgsrc",
            prodcat=self.prodcat,
            vend=self.vend,
        )
        self.cust=get_user_model().objects.create_user(
            username="username",
            password="password",
        )
        self.order = Order.objects.create(
            cust=self.cust,
            prod=self.prod,
            order_quantity=99,
            order_totalprice=99 * self.prod.prod_price,
        )


    def test_model_field_value(self):
        self.assertEqual(self.prodcat.prodcat_name, "prodcat_name")
        self.assertEqual(self.vend.vend_name, "vend_name")
        self.assertEqual(self.vend.vend_country, "TW")
        self.assertEqual(self.vend.vend_city, "vend_city")
        self.assertEqual(self.prod.prod_name, "prod_name")
        self.assertEqual(self.prod.prod_desc, "prod_desc")
        self.assertEqual(self.prod.prod_price, 3.14)
        self.assertEqual(self.prod.prod_imgname, "hamburger.jpg")
        self.assertEqual(self.prod.prod_imgsrc, "prod_imgsrc")
        self.assertEqual(self.prod.prodcat, self.prodcat)
        self.assertEqual(self.prod.vend, self.vend)
        self.assertEqual(self.cust.username, "username")
        self.assertEqual(self.order.cust, self.cust)
        self.assertEqual(self.order.prod, self.prod)
        self.assertEqual(self.order.order_quantity, 99)
        self.assertEqual(self.order.order_totalprice, 99 * 3.14)


    def test_string_representation(self):
        self.assertEqual(str(self.prodcat), self.prodcat.prodcat_name)
        self.assertEqual(str(self.vend), self.vend.vend_name)
        self.assertEqual(str(self.prod), self.prod.prod_name)
        self.assertEqual(str(self.order), f"Order ID {self.order.id}")


    def test_get_absolute_url(self):
        self.assertEqual(
            self.prod.get_absolute_url(),
            f'/shop/products/{self.prod.id}/',
        )


    # views
    def test_product_categories_view(self):
        response = self.client.get(
            reverse('product_categories'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_categories.html')


    def test_product_category_products_view(self):
        response = self.client.get(
            reverse('product_category_products', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_category_products.html')

        response = self.client.get(
            reverse('product_category_products', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')


    def test_vendors_view(self):
        response = self.client.get(
            reverse('vendors'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/vendors.html')


    def test_vendor_products_view(self):
        response = self.client.get(
            reverse('vendor_products', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/vendor_products.html')

        response = self.client.get(
            reverse('vendor_products', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')


    def test_products_view(self):
        response = self.client.get(reverse('products'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/products.html')


    def test_product_view___get___not_logged_in(self):
        response = self.client.get(
            reverse('product', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product.html')

        response = self.client.get(
            reverse('product', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')


    def test_product_view___get___logged_in(self):
        self.client.login(username='username', password='password')

        response = self.client.get(
            reverse('product', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product.html')

        response = self.client.get(
            reverse('product', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')


    def test_product_view___post___not_logged_in(self):
        response = self.client.post(
            reverse('product', args=['1']),
            data={'order_quantity': 1},
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product.html')

        response = self.client.post(
            reverse('product', args=['99999']),
            data={'order_quantity': 1},
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')


    def test_product_view___post___logged_in(self):
        self.client.login(username='username', password='password')

        response = self.client.post(
            reverse('product', args=['1']),
            data={'order_quantity': 1},
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product.html')

        response = self.client.post(
            reverse('product', args=['99999']),
            data={'order_quantity': 1},
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')
