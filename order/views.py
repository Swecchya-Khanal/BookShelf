# views.py in your order app

from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from Book.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from Book.models import Book, MyRating

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


@login_required
def rate_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Handle the rating form submission
        rating_value = int(request.POST.get('rating', 0))

        if 1 <= rating_value <= 5:
            # Check if the user has already rated the book
            existing_rating = MyRating.objects.filter(user=request.user, book=book).first()

            if existing_rating:
                # Update the existing rating
                existing_rating.ratingno = rating_value
                existing_rating.save()
            else:
                # Create a new rating
                MyRating.objects.create(user=request.user, book=book, ratingno=rating_value)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'rate_book.html', {'book': book})