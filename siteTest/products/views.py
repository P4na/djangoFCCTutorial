from django.shortcuts import render
from .models import Product

def productsView(request):
    products = Product.objects.all()
    context = {"products":products,}
    return render(request, "products.html", context)

def productDetailView(request):
    context = {}
    return render(request, 'productDetail.html', context)
