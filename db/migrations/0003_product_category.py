# Generated by Django 4.0.5 on 2023-02-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_remove_buyer_buyer_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='none', max_length=100),
        ),
    ]