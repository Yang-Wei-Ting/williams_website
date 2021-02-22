import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Product
from .forms import OrderForm


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


def product_detail_view(request, pk):
    prod = Product.objects.get(id=pk)
    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour
    purchased = False
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.cust_id = request.user
                order.prod_id = prod
                order.order_totalprice = prod.prod_price * form.cleaned_data['order_quantity']
                order.save()
                purchased = True
        else:
            form = OrderForm()

    return render(request, 'shop/product_detail.html', locals())
