import datetime
from django.shortcuts import render

from .models import Product
from .forms import OrderForm


current_time = datetime.datetime.now()
current_hour = current_time.timetuple().tm_hour
prods = Product.objects.all()


def product_list_view(request, browse_by):
    if browse_by == 'Category':
        '''
        SELECT shop_product.*
        FROM shop_product INNER JOIN shop_productcategory
          ON shop_product.prodcat_id_id = shop_productcategory.id
        WHERE shop_productcategory.prodcat_name = '?????';
        '''
        prodcat_names = ("Books, Movies & Music", "Business & Industrial",
                         "Collectibles & Art", "Electronics", "Fashion", "Food",
                         "Health & Beauty", "Home & Garden", "Motors",
                         "Sporting Goods", "Toys & Hobbies", "Others")
        prods_group = (prods.filter(prodcat_id__prodcat_name=prodcat_name) for prodcat_name in prodcat_names)

    elif browse_by == 'Vendor':
        '''
        SELECT shop_product.*
        FROM shop_product INNER JOIN shop_vendor
          ON shop_product.vend_id_id = shop_vendor.id
        WHERE shop_vendor.vend_name = '?????';
        '''
        vend_names = ("Abibas", "Banana", "F 4 Fashion", "Fink Manufacturing",
                      "Microhard", "Mike", "Penguin Inc", "Programing Press",
                      "Ryan Industries", "Toys R Them", "WcDonald's", "Unknown")
        prods_group = (prods.filter(vend_id__vend_name=vend_name) for vend_name in vend_names)

    context = {
        'browse_by': browse_by,
        'current_time': current_time,
        'current_hour': current_hour,
        'prods_group': prods_group,
    }
    return render(request, 'shop/product_list.html', context=context)


def product_detail_view(request, pk):
    prod = prods.get(id=pk)
    purchased, order, form = False, None, None

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

    context = {
        'prod': prod,
        'current_time': current_time,
        'current_hour': current_hour,
        'purchased': purchased,
        'order': order,
        'form': form,
    }
    return render(request, 'shop/product_detail.html', context=context)
