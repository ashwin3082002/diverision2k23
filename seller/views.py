from django.shortcuts import render, redirect
from db.models import Seller, Buyer, Product, Order, Transactions
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from util.func import send_sms

# Create your views here.

def seller_index(request):
    return render(request, 'index.html')

@login_required(login_url='seller_login')
def seller_index(request):
    seller_id = Seller.objects.get(seller_email=request.user.username).seller_id
    orders = Order.objects.filter(seller_id= seller_id)
    context = {'orders':orders[:3],"order_count":orders.count(),"products_listed":Product.objects.filter(seller_id=seller_id).count(),"total_sold":orders.filter(order_status="Delivered").count()}
    return render(request, 'seller/index.html', context)

@login_required(login_url='seller_login')
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST['product_description']
        product_photo = request.FILES['product_image']
        category = request.POST['product_category']

        seller_id =  Seller.objects.get(seller_email=request.user.username)
        product = Product(product_name=product_name, product_price=product_price, product_description=product_description, product_photo=product_photo, seller_id=seller_id, category=category)
        product.save()
        send_sms(f"""
New product was added to your seller Account
         
Product Name: {product_name}
Product Price: {product_price}

The product is listed succesfully in the website!!  

Regards,
Team Safypay
   """, seller_id.seller_phone)
        
        messages.success(request, 'Product added successfully')
        return redirect('seller_index')
    return render(request, 'seller/add_product.html')

@login_required(login_url='seller_login')
def list_product(request):
    seller_id =  Seller.objects.get(seller_email=request.user.username)
    product = Product.objects.filter(seller_id=seller_id)
    context = {'products':product, "empty":product.first()}
    return render(request, 'seller/list_product.html', context)

@login_required(login_url='seller_login')
def view_product(request, id):
    product = Product.objects.get(product_id=id)

    if "edit" in request.POST:
        return redirect('edit_product', id=id)
    
    if "delete" in request.POST:
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('list_product')
    
    context = {'product':product}
    return render(request, 'seller/view_product.html', context)

@login_required(login_url='seller_login')
def edit_product(request, id):
    product = Product.objects.get(product_id=id)
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST['product_description']
        product_photo = request.FILES['product_image']
        category = request.POST['product_category']

        product.product_name = product_name
        product.product_price = product_price
        product.product_description = product_description
        product.product_photo = product_photo
        product.category = category
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('view_product', id=id)
    context = {'product':product}
    return render(request, 'seller/edit_product.html', context)

@login_required(login_url='seller_login')
def orders(request):
    seller_id =  Seller.objects.get(seller_email=request.user.username)
    order = Order.objects.filter(product_id__seller_id=seller_id)
    context = {'orders':order, "empty":order.first()}
    return render(request, 'seller/orders.html', context)


def seller_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seller_index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('seller_login')
    return render(request, 'seller/login.html')

def seller_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('seller_login')

def seller_wallet(request):
    seller = Seller.objects.get(seller_email=request.user.username)
    transaction = Transactions.objects.filter(seller_id=seller)

    context = {'seller':seller, 'transactions':transaction}

    
    return render(request, 'seller/wallet.html', context)


def buyer_wallet(request):
    buyer = Buyer.objects.get(buyer_email=request.user.username)
    transaction = Transactions.objects.filter(buyer_id=Buyer).all()

    context = {'buyer':buyer, 'transactions':transaction}

    
    return render(request, 'buyer/wallet.html', context)

