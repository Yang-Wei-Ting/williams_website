# Generated by Django 3.1.7 on 2021-02-27 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodcat_name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ('prodcat_name',),
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vend_name', models.CharField(max_length=100, verbose_name='Name')),
                ('vend_country', models.CharField(choices=[('AQ', 'Antarctica'), ('AU', 'Australia'), ('AT', 'Austria'), ('BE', 'Belgium'), ('BR', 'Brazil'), ('CA', 'Canada'), ('CG', 'Congo'), ('CU', 'Cuba'), ('DK', 'Denmark'), ('EG', 'Egypt'), ('FI', 'Finland'), ('FR', 'France'), ('DE', 'Germany'), ('GR', 'Greece'), ('HU', 'Hungary'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IT', 'Italy'), ('MY', 'Malaysia'), ('NO', 'Norway'), ('CN', "People's Republic of China"), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('TW', 'Republic of China (Taiwan)'), ('KR', 'Republic of Korea'), ('SA', 'Saudi Arabia'), ('SG', 'Singapore'), ('ZA', 'South Africa'), ('ES', 'Spain'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('TH', 'Thailand'), ('TR', 'Turkey'), ('GB', 'United Kingdom'), ('US', 'United States of America'), ('VN', 'Viet Nam'), ('XX', 'Unknown')], default='TW', max_length=2, verbose_name='Country')),
                ('vend_city', models.CharField(max_length=100, verbose_name='City')),
            ],
            options={
                'ordering': ('vend_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100, verbose_name='Name')),
                ('prod_desc', models.TextField(verbose_name='Description')),
                ('prod_price', models.FloatField(verbose_name='Price (NTD)')),
                ('prod_imgname', models.CharField(max_length=100, verbose_name='Image File Name')),
                ('prod_imgsrc', models.TextField(verbose_name='Image Source')),
                ('prodcat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productcategory')),
                ('vend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.vendor')),
            ],
            options={
                'ordering': ('prod_name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('order_totalprice', models.PositiveIntegerField(verbose_name='Total Price')),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]