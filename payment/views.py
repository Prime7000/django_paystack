from django.shortcuts import render, redirect
from django.conf import settings
from product.models import Place_order
from .models import Payment
from django.contrib import messages

# Create your views here.

def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()
    if verified:
        pk = request.session['order_id']
        order = Place_order.objects.get(pk=pk)
        order.is_verified == True
        order.save()
        messages.success(request, 'Payment was successful')
        return render(request, 'sucess.html', {})

    else:
        messages.warning(request, 'Payment was not successful')
        return redirect('core:home')
