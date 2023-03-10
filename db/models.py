from django.db import models

# Create your models here.
class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField(max_length=100)
    seller_phone = models.CharField(max_length=100)
    seller_photo = models.ImageField(upload_to='seller_photo', blank=True, null=True)
    seller_status = models.CharField(max_length=100, default='pending')
    seller_wallet = models.CharField(max_length=100, default='0')

    def __str__(self):
        return self.seller_name
    
class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField(max_length=100)
    buyer_phone = models.CharField(max_length=100)
    buyer_photo = models.ImageField(upload_to='buyer_photo', blank=True, null=True)
    buyer_status = models.CharField(max_length=100, default='pending')
    buyer_wallet = models.CharField(max_length=100, default='0')

    def __str__(self):
        return self.buyer_name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_photo = models.ImageField(upload_to='product_photo', blank=True, null=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now=True)
    order_status = models.CharField(max_length=255, default='created')
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='none')
    transaction_status = models.CharField(max_length=100, default='holding', choices=(('holding', 'holding'), ('refunded', 'refunded'), ('paid', 'paid')))
    status = models.CharField(max_length=100,default="created")

    def __str__(self):
        return self.order_status
    

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateField(auto_now=True)
    transaction_amount = models.CharField(max_length=100)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.transaction_id)

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=100, default='Processing')
    dispute = models.BooleanField(default=False)
    dispute_reason = models.CharField(max_length=100, default=None, blank=True, null=True)
    disputed_by = models.CharField(max_length=100, default=None, blank=True, null=True, choices=(('buyer', 'buyer'), ('seller', 'seller')))
    solved_dispute = models.CharField(max_length=20, default=None, blank=True, null=True, choices=(('yes', 'yes'), ('no', 'no')))
    wronged_party = models.CharField(max_length=20, default=None, blank=True, null=True, choices=(('buyer', 'buyer'), ('seller', 'seller')))


    def __str__(self):
        return self.delivery_status