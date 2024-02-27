from django.shortcuts import render, redirect
from .models import Product
from .forms import Place_order
from django.contrib import messages

from django.conf import settings
from payment.models import Payment

def detail(request, pk):
    product = Product.objects.get(pk=pk)

    return render(request, 'index.html',{
        'item': product,
    })


def place_order(request):
    pk = 1
    if request.method == 'POST':
        # product_id = request.POST.get('product_id')
        form = Place_order(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            product = Product.objects.get(pk=pk)
            var.product = product
            var.user = request.user
            var.total_cost = int(product.price) * int(var.item_amount)
            var.save() 

            # the payment algorithm
            payment = Payment.objects.create(amount = var.total_cost, user = request.user, email = request.user.email)
            payment.save()
            public_key = settings.PAYSTACK_PUBLIC_KEY
            request.session['order_id'] = var.id

            return render(request,'make_payment.html',{
                'total_cost': var.total_cost,
                'item_amount': var.item_amount,
                'product': product,
                'payment': payment,
                'paystack_pub_key': public_key,
                'amount': payment.amount_value(),
            })
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('product:home')
    else:
        form = Place_order()
        return render(request,'place_order.html',{
            'form': form,
        })
    
def home(request):
    return render(request, 'index.html',{})

        

    