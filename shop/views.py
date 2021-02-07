import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User

from .models import Product, Order


def product_category_list_view(request):
    prods = Product.objects.all()
    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour

    '''
    SELECT shop_product.*
    FROM shop_product INNER JOIN shop_productcategory
      ON shop_product.prodcat_id_id = shop_productcategory.id
    WHERE shop_productcategory.prodcat_name = '?????';
    '''

    books_movies_music__prods  = a = prods.filter(prodcat_id__prodcat_name="Books, Movies & Music")
    business_industrial__prods = b = prods.filter(prodcat_id__prodcat_name="Business & Industrial")
    collectibles_art__prods    = c = prods.filter(prodcat_id__prodcat_name="Collectibles & Art")
    electronics__prods         = d = prods.filter(prodcat_id__prodcat_name="Electronics")
    fashion__prods             = e = prods.filter(prodcat_id__prodcat_name="Fashion")
    food__prods                = f = prods.filter(prodcat_id__prodcat_name="Food")
    health_beauty__prods       = g = prods.filter(prodcat_id__prodcat_name="Health & Beauty")
    home_garden__prods         = h = prods.filter(prodcat_id__prodcat_name="Home & Garden")
    motors__prods              = i = prods.filter(prodcat_id__prodcat_name="Motors")
    sportinggoods__prods       = j = prods.filter(prodcat_id__prodcat_name="Sporting Goods")
    toys_hobbies__prods        = k = prods.filter(prodcat_id__prodcat_name="Toys & Hobbies")
    others__prods              = l = prods.filter(prodcat_id__prodcat_name="Others")

    prods_group = (a, b, c, d, e, f, g, h, i, j, k, l)

    return render(request, 'shop/product_category_list.html', locals())


def product_vendor_list_view(request):
    prods = Product.objects.all()
    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour

    '''
    SELECT shop_product.*
    FROM shop_product INNER JOIN shop_vendor
      ON shop_product.vend_id_id = shop_vendor.id
    WHERE shop_vendor.vend_name = '?????';
    '''

    abibas__prods     = a = prods.filter(vend_id__vend_name="Abibas")
    banana__prods     = b = prods.filter(vend_id__vend_name="Banana")
    f4fashion__prods  = c = prods.filter(vend_id__vend_name="F 4 Fashion")
    fink__prods       = d = prods.filter(vend_id__vend_name="Fink Manufacturing")
    microhard__prods  = e = prods.filter(vend_id__vend_name="Microhard")
    mike__prods       = f = prods.filter(vend_id__vend_name="Mike")
    penguin__prods    = g = prods.filter(vend_id__vend_name="Penguin Inc")
    programing__prods = h = prods.filter(vend_id__vend_name="Programing Press")
    ryan__prods       = i = prods.filter(vend_id__vend_name="Ryan Industries")
    toysrthem__prods  = j = prods.filter(vend_id__vend_name="Toys R Them")
    wcdonalds__prods  = k = prods.filter(vend_id__vend_name="WcDonald's")
    unknown__prods    = l = prods.filter(vend_id__vend_name="Unknown")

    prods_group = (a, b, c, d, e, f, g, h, i, j, k, l)

    return render(request, 'shop/product_vendor_list.html', locals())


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'prod'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now()
        context['current_time'] = current_time
        context['current_hour'] = current_time.timetuple().tm_hour
        return context


def order_view(request, pk):
    try:
        cust = User.objects.get(id=request.user.id)
        prod = Product.objects.get(id=pk)
        order_quantity = int(request.POST["order_quantity"])
        order_totalprice = prod.prod_price * order_quantity
        order = Order.objects.create(
            cust_id=cust,
            prod_id=prod,
            order_quantity=order_quantity,
            order_totalprice=order_totalprice
        )
    except (User.DoesNotExist, Product.DoesNotExist, KeyError):
        return HttpResponseRedirect("/")

    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour

    return render(request, 'shop/order.html', locals())
