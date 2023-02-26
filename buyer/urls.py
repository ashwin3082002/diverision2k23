"""safepay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.buyer_index, name='buyer_index'),
    path('buyer_login/',views.buyer_login, name='buyer_login'),
    path('cart/',views.cart_page, name='cart_page'),
    path('checkout/',views.checkout_page, name='checkout_page'),
    path('home/',views.home_page, name='home_page'),
    path('orderconfirm/',views.orderconfirm_page, name='orderconfirm_page'),
    path('orders/',views.orders_page, name='orders_page'),
    path('wallet/',views.wallet_page, name='wallet_page'),
]