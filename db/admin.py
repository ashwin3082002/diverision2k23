from django.contrib import admin
from db.models import Seller, Buyer, Product, Order, Transactions
# Register your models here.

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Transactions)
