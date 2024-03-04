from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
""" from .models import Contact
from .forms import ContactForm """

def contact(request):
  """   if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent! We will get back to you soon.')
            return redire ct('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm() """
  return render(request, 'contact_us.html')