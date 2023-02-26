from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='buyer_index'),
    path('buyer_login/',views.buyer_login, name='buyer_login'),
    path('cart/',views.cart_page, name='cart_page'),
    path('checkout/',views.checkout_page, name='checkout_page'),
    path('home/',views.home_page, name='home_page'),
    path('orderconfirm/',views.orderconfirm_page, name='orderconfirm_page'),
    path('orders/',views.orders_page, name='orders_page'),
    path('wallet/',views.wallet_page, name='wallet_page'),
]