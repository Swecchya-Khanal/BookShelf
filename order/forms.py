# forms.py in the order app
from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    payment_option = forms.ChoiceField(choices=[('cash_on_delivery', 'Cash on Delivery')], required=True)
