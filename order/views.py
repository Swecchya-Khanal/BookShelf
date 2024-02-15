# views.py in your order app

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from Book.models import Book

@login_required
def create_order(request):
    cart_items = request.session.get('cart', {}).values()

    # Calculate the total price and subtotal for each cart item
    total_price = sum(item['quantity'] * item['book']['price'] for item in cart_items)
    
    for cart_item in cart_items:
        cart_item['subtotal'] = cart_item['quantity'] * cart_item['book']['price']

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                user=request.user,
                total_price=total_price,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address']
            )
            order.save()
            order.books.set(Book.objects.filter(pk__in=request.session['cart'].keys()))

            # Clear the cart after creating the order
            request.session['cart'] = {}

            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

@login_required
def my_order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_order_list.html', {'orders': orders})