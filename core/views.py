from django.shortcuts import render
from product.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all().order_by('id')

    return render(request,'home.html',{
        'items': products,
    }) 

