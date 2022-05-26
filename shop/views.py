import datetime

from django.db.models import BooleanField, Case, When
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import OrderForm
from .models import Product, ProductCategory, Vendor


def get_current_time_and_hour():
    '''
    Returns a dictionary containing current_time and current_hour.
    '''
    current_time = datetime.datetime.now()
    current_hour = current_time.timetuple().tm_hour
    return {'current_time': current_time, 'current_hour': current_hour}


class ProductCategoriesView(ListView):
    '''
    A view that displays all product categories.
    '''
    queryset = ProductCategory.objects.annotate(
        is_others=Case(
            When(prodcat_name__exact='Others', then=True),
            default=False,
            output_field=BooleanField(),
        ),
    ).order_by('is_others', 'prodcat_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_current_time_and_hour())
        return context

    def get_template_names(self):
        return 'shop/product_categories.html'


class ProductCategoryProductsView(ListView):
    '''
    A view that displays all products of a specific product category.
    '''
    def get_queryset(self):
        self.prodcat = get_object_or_404(ProductCategory, id=self.kwargs['pk'])
        return Product.objects.filter(prodcat=self.prodcat)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_category'] = self.prodcat
        context.update(get_current_time_and_hour())
        return context

    def get_template_names(self):
        return 'shop/product_category_products.html'


class VendorsView(ListView):
    '''
    A view that displays all vendors.
    '''
    queryset = Vendor.objects.annotate(
        is_unknown=Case(
            When(vend_name__exact='Unknown', then=True),
            default=False,
            output_field=BooleanField(),
        ),
    ).order_by('is_unknown', 'vend_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_current_time_and_hour())
        return context

    def get_template_names(self):
        return 'shop/vendors.html'


class VendorProductsView(ListView):
    '''
    A view that displays all products of a specific vendor.
    '''
    def get_queryset(self):
        self.vend = get_object_or_404(Vendor, id=self.kwargs['pk'])
        return Product.objects.filter(vend=self.vend)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendor'] = self.vend
        context.update(get_current_time_and_hour())
        return context

    def get_template_names(self):
        return 'shop/vendor_products.html'


class ProductsView(ListView):
    '''
    A view that displays all products.
    '''
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_current_time_and_hour())
        return context

    def get_template_names(self):
        return 'shop/products.html'


def product_view(request, pk):
    '''
    A view that displays details of a specific product.
    If an user is authenticated, he or she can order the product.
    '''
    product = get_object_or_404(Product, id=pk)
    form, order, purchased = None, None, False

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.cust = request.user
                order.prod = product
                order.order_totalprice = product.prod_price * form.cleaned_data['order_quantity']
                order.save()
                purchased = True
        else:
            form = OrderForm()

    context = {
        'product': product,
        'form': form,
        'order': order,
        'purchased': purchased,
        **get_current_time_and_hour(),
    }
    return render(request, 'shop/product.html', context=context)
