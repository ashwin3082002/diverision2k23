from django.shortcuts import render

# Create your views here.
def buyer_index(request):
    return render(request, 'buyer/index.html')