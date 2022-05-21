from django.db import models
from django.urls import reverse

COUNTRY_CHOICES = [
    ('AQ', 'Antarctica'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('BE', 'Belgium'),
    ('BR', 'Brazil'),
    ('CA', 'Canada'),
    ('CG', 'Congo'),
    ('CU', 'Cuba'),
    ('DK', 'Denmark'),
    ('EG', 'Egypt'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('GR', 'Greece'),
    ('HU', 'Hungary'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IT', 'Italy'),
    ('MY', 'Malaysia'),
    ('NO', 'Norway'),
    ('CN', "People's Republic of China"),
    ('PH', 'Philippines'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('TW', 'Republic of China (Taiwan)'),
    ('KR', 'Republic of Korea'),
    ('SA', 'Saudi Arabia'),
    ('SG', 'Singapore'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('TH', 'Thailand'),
    ('TR', 'Turkey'),
    ('GB', 'United Kingdom'),
    ('US', 'United States of America'),
    ('VN', 'Viet Nam'),
    ('XX', 'Unknown'),
]


class ProductCategory(models.Model):

    prodcat_name = models.CharField("Name", max_length=100)

    class Meta:

        ordering = ('prodcat_name', )

    def __str__(self):
        return self.prodcat_name


class Vendor(models.Model):

    vend_name    = models.CharField("Name", max_length=100)
    vend_country = models.CharField("Country", max_length=2, choices=COUNTRY_CHOICES, default='TW')
    vend_city    = models.CharField("City", max_length=100)

    class Meta:

        ordering = ('vend_name', )

    def __str__(self):
        return self.vend_name


class Product(models.Model):

    prod_name    = models.CharField("Name", max_length=100)
    prod_desc    = models.TextField("Description")
    prod_price   = models.FloatField("Price (NTD)")
    prod_imgname = models.CharField("Image File Name", max_length=100)
    prod_imgsrc  = models.TextField("Image Source")
    prodcat      = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    vend         = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:

        ordering = ('prod_name', )

    def __str__(self):
        return self.prod_name

    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])


class Order(models.Model):

    cust             = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    prod             = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity   = models.PositiveIntegerField("Quantity")
    order_totalprice = models.PositiveIntegerField("Total Price")
    order_date       = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return f"Order ID {self.id}"
