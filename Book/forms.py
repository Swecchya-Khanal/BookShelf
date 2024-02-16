# yourapp/forms.py
from django import forms
from .models import Author, Category

class BookFilterForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False, empty_label="All Authors")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="All Categories")
