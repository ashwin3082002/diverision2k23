# Generated by Django 4.0.5 on 2023-02-25 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_id', models.AutoField(primary_key=True, serialize=False)),
                ('buyer_name', models.CharField(max_length=100)),
                ('buyer_email', models.EmailField(max_length=100)),
                ('buyer_password', models.CharField(max_length=100)),
                ('buyer_phone', models.CharField(max_length=100)),
                ('buyer_address', models.CharField(max_length=100)),
                ('buyer_city', models.CharField(max_length=100)),
                ('buyer_state', models.CharField(max_length=100)),
                ('buyer_pincode', models.CharField(max_length=100)),
                ('buyer_photo', models.ImageField(blank=True, null=True, upload_to='media/buyer_photo')),
                ('buyer_status', models.CharField(default='pending', max_length=100)),
                ('buyer_wallet', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_email', models.EmailField(max_length=100)),
                ('seller_password', models.CharField(max_length=100)),
                ('seller_phone', models.CharField(max_length=100)),
                ('seller_address', models.CharField(max_length=100)),
                ('seller_city', models.CharField(max_length=100)),
                ('seller_state', models.CharField(max_length=100)),
                ('seller_pincode', models.CharField(max_length=100)),
                ('seller_photo', models.ImageField(blank=True, null=True, upload_to='media/seller_photo')),
                ('seller_status', models.CharField(default='pending', max_length=100)),
                ('seller_wallet', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
                ('product_photo', models.ImageField(blank=True, null=True, upload_to='media/product_photo')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(default='created', max_length=255)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.buyer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.product')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.seller')),
            ],
        ),
    ]
