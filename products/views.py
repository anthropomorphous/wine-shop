from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
#from cart.forms import CartAddProductForm


def index(request):
    products = Product.objects.all()
   # cart_product_form = CartAddProductForm()
    return render(request, 'index.html', {'products': products})



def detail(request):
    context = {}
    return render(request, 'detail.html', context)


def new(request):
    return HttpResponse('New Products')


def about(request):
    context = {}
    return render(request, 'about.html', context)






