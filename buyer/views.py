from django.shortcuts import render, redirect
from db.models import Seller, Buyer, Product, Order, Transactions
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from util.func import send_sms
from django.contrib.auth.models import User

# Create your views here.
def buyer_index(request):
    return render(request, 'buyer/home.html')

def buyer_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('buyer_login')


    return render(request, 'buyer/login.html')

def cart_page(request):
    return render(request, 'buyer/cart.html')

def checkout_page(request):
    return render(request, 'buyer/checkout.html')

def home_page(request):
    return render(request, 'buyer/home.html')

def orderconfirm_page(request):
    return render(request, 'buyer/orderconfirm.html')

def orders_page(request):
    return render(request, 'buyer/orders.html')

def wallet_page(request):
    return render(request, 'buyer/wallet.html')