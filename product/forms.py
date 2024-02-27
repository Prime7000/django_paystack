from .models import Place_order
from django import forms

class Place_order(forms.ModelForm):
    class Meta:
        model = Place_order
        fields = (  'item_amount', 'full_name', 'phone_number','delivery_address')