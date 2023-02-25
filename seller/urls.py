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
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.seller_index, name='seller_index'),
    path('login',views.seller_login, name='seller_login'),
    path('logout',views.seller_logout, name='seller_logout'),

    path('add/product',views.add_product, name='add_product'),
    path('view/product',views.view_product, name='view_product'),
    path('product_edit/<int:id>',views.edit_product, name='edit_product'),
]
