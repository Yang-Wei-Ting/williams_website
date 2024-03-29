from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Order, Product, ProductCategory, Vendor
from .views import (ProductCategoriesView, ProductCategoryProductsView,
                    ProductsView, VendorProductsView, VendorsView)


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
            prod_imgname="hamburger.jpg",
            prod_imgsrc="prod_imgsrc",
            prodcat=self.prodcat,
            vend=self.vend,
        )
        self.cust = get_user_model().objects.create_user(
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
            reverse('product', args=[str(self.prod.id)]),
        )


class ShopViewsTest(TestCase):

    fixtures = ['shop.json']

    def test_product_categories_view__get_200(self):
        response = self.client.get(
            reverse('product_categories'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['view'], ProductCategoriesView))
        self.assertEqual(response.context['view']._allowed_methods(), ['GET', 'HEAD', 'OPTIONS'])
        self.assertQuerysetEqual(
            response.context['object_list'],
            [
                'Books', 'Electronics', 'Fashion', 'Food', 'Health & Beauty', 'Sporting Goods',
                'Toys & Hobbies', 'Others',
            ],
            transform=lambda obj: obj.prodcat_name,
            ordered=True,
        )
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product_categories.html')

    def test_product_category_products_view__get_200(self):
        response = self.client.get(
            reverse('product_category_products', args=['12']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['view'], ProductCategoryProductsView))
        self.assertEqual(response.context['view']._allowed_methods(), ['GET', 'HEAD', 'OPTIONS'])
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['French Fries', 'Hamburger', 'Ice Cubes'],
            transform=lambda obj: obj.prod_name,
            ordered=True,
        )
        self.assertEqual(response.context['product_category'].prodcat_name, 'Food')
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product_category_products.html')

    def test_product_category_products_view__get_404(self):
        response = self.client.get(
            reverse('product_category_products', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')

    def test_vendors_view__get_200(self):
        response = self.client.get(
            reverse('vendors'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['view'], VendorsView))
        self.assertEqual(response.context['view']._allowed_methods(), ['GET', 'HEAD', 'OPTIONS'])
        self.assertQuerysetEqual(
            response.context['object_list'],
            [
                'Abibas', 'Banana', 'F 4 Fashion', 'Fink Manufacturing', 'Microhard', 'Mike',
                'Penguin Inc.', 'Programing Press', 'Toys R Them', "WcDonald's", 'Unknown',
            ],
            transform=lambda obj: obj.vend_name,
            ordered=True,
        )
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/vendors.html')

    def test_vendor_products_view__get_200(self):
        response = self.client.get(
            reverse('vendor_products', args=['5']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['view'], VendorProductsView))
        self.assertEqual(response.context['view']._allowed_methods(), ['GET', 'HEAD', 'OPTIONS'])
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['French Fries', 'Hamburger'],
            transform=lambda obj: obj.prod_name,
        )
        self.assertEqual(response.context['vendor'].vend_name, "WcDonald's")
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/vendor_products.html')

    def test_vendor_products_view__get_404(self):
        response = self.client.get(
            reverse('vendor_products', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')

    def test_products_view__get_200(self):
        response = self.client.get(
            reverse('products'),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['view'], ProductsView))
        self.assertEqual(response.context['view']._allowed_methods(), ['GET', 'HEAD', 'OPTIONS'])
        self.assertQuerysetEqual(
            response.context['object_list'],
            [
                '!phone 20', 'Dinosaur Plush Toy', 'Doors 12', 'Doors 98', 'Flying Shoes',
                'Fountain of Youth', 'French Fries', 'Hamburger', 'Ice Cubes', 'Mask',
                'Sky-Hook', 'Sneakers', 'Three Scoops of Django 4.2',
            ],
            transform=lambda obj: obj.prod_name,
        )
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/products.html')

    def test_product_view__get_200(self):
        response = self.client.get(
            reverse('product', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'].prod_name, 'Sneakers')
        self.assertIsNone(response.context['form'])
        self.assertIsNone(response.context['order'])
        self.assertFalse(response.context['purchased'])
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product.html')

        # Login
        user = get_user_model().objects.create_user(
            username='username',
            password='password',
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse('product', args=['1']),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'].prod_name, 'Sneakers')
        self.assertFalse(response.context['form'].is_bound)
        self.assertIsNone(response.context['order'])
        self.assertFalse(response.context['purchased'])
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product.html')

    def test_product_view__get_404(self):
        response = self.client.get(
            reverse('product', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')

        # Login
        user = get_user_model().objects.create_user(
            username='username',
            password='password',
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse('product', args=['99999']),
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')

    def test_product_view__post_200(self):
        response = self.client.post(
            reverse('product', args=['1']),
            data={'order_quantity': 2},
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'].prod_name, 'Sneakers')
        self.assertIsNone(response.context['form'])
        self.assertIsNone(response.context['order'])
        self.assertFalse(response.context['purchased'])
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product.html')

        # Login
        user = get_user_model().objects.create_user(
            username='username',
            password='password',
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('product', args=['1']),
            data={'order_quantity': 2},
            secure=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'].prod_name, 'Sneakers')
        self.assertIn('form', response.context)
        order = Order.objects.last()
        self.assertEqual(order.cust.username, 'username')
        self.assertEqual(order.prod.prod_name, 'Sneakers')
        self.assertEqual(order.order_quantity, 2)
        self.assertEqual(order.order_totalprice, 7000)
        self.assertTrue(response.context['purchased'])
        self.assertIn('current_time', response.context)
        self.assertIn('current_hour', response.context)
        self.assertTemplateUsed(response, 'shop/product.html')

    def test_product_view__post_404(self):
        response = self.client.post(
            reverse('product', args=['99999']),
            data={'order_quantity': 2},
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')

        # Login
        user = get_user_model().objects.create_user(
            username='username',
            password='password',
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('product', args=['99999']),
            data={'order_quantity': 2},
            secure=True,
        )
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'home/page_not_found.html')
