from django.db import models

# Create your models here.
class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField(max_length=100)
    seller_password = models.CharField(max_length=100)
    seller_phone = models.CharField(max_length=100)
    seller_address = models.CharField(max_length=100)
    seller_city = models.CharField(max_length=100)
    seller_state = models.CharField(max_length=100)
    seller_pincode = models.CharField(max_length=100)
    seller_photo = models.ImageField(upload_to='media/seller_photo', blank=True, null=True)
    seller_status = models.CharField(max_length=100, default='pending')
    seller_wallet = models.CharField(max_length=100, default='0')

    def __str__(self):
        return self.seller_name
    
class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField(max_length=100)
    buyer_password = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=100)
    buyer_address = models.CharField(max_length=100)
    buyer_city = models.CharField(max_length=100)
    buyer_state = models.CharField(max_length=100)
    buyer_pincode = models.CharField(max_length=100)
    buyer_photo = models.ImageField(upload_to='media/buyer_photo', blank=True, null=True)
    buyer_status = models.CharField(max_length=100, default='pending')
    buyer_wallet = models.CharField(max_length=100, default='0')

    def __str__(self):
        return self.buyer_name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_photo = models.ImageField(upload_to='media/product_photo', blank=True, null=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    order_status = models.CharField(max_length=255, default='created')
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_status