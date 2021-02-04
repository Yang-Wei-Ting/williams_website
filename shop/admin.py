from django.contrib import admin

from .models import ProductCategory, Vendor, Product, Order


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("prodcat_name",)
    ordering = ("prodcat_name",)


class VendorAdmin(admin.ModelAdmin):
    list_display = ("vend_name", "vend_country", "vend_city")
    ordering = ("vend_name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "prod_name",
        "prod_desc",
        "prod_price",
        "prod_imgname",
        "prod_imgsrc",
        "prodcat",
        "vend",
    )
    ordering = ("prod_name",)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "cust",
        "prod",
        "order_quantity",
        "order_totalprice",
        "order_date",
    )
    ordering = ("-order_date",)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
