from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.seller_index, name='seller_index'),
    path('login',views.seller_login, name='seller_login'),
    path('logout',views.seller_logout, name='seller_logout'),

    path('add/product',views.add_product, name='add_product'),
    path('product_listing',views.list_product, name='list_product'),
    path('product_view/<int:id>',views.view_product, name='view_product'),
    path('product_edit/<int:id>',views.edit_product, name='edit_product'),

    path('orders',views.orders, name='orders'),

    path('wallet', views.seller_wallet, name='seller_wallet'),

    path('buyer', views.buyer_wallet, name='buyer_wallet'),
]

