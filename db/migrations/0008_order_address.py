# Generated by Django 4.1.7 on 2023-02-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_remove_buyer_buyer_address_remove_buyer_buyer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
