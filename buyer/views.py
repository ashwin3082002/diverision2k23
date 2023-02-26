from django.shortcuts import render

# Create your views here.
def buyer_index(request):
    return render(request, 'buyer/index.html')

def buyer_login(request):
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