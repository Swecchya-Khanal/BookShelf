from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from Book.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Book.models import Book, MyRating
from django.db import models
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

    # Check if the user has ordered the book
    has_ordered = Order.objects.filter(user=request.user, books=book).exists()

    if not has_ordered:
        # Redirect to a page indicating that the user needs to order the book first
        return render(request, 'order_required.html', {'book': book})
    
    existing_rating = MyRating.objects.filter(user=request.user, book=book).first()

         
    if request.method == 'POST':
        # Handle the rating form submission
        rating_value = int(request.POST.get('rating', 0))
         
        

        if 1 <= rating_value <= 5:
            # Check if the user has already rated the book
           

            if existing_rating:
                # Update the existing rating
                existing_rating.rating_no = rating_value
                existing_rating.save()
            else:
                # Create a new rating
                MyRating.objects.create(user=request.user, book=book, rating_no=rating_value)

            return HttpResponseRedirect(reverse('order:my_order_list'))

    return render(request, 'rate_book.html', { 'book': book, 'existing_rating': existing_rating})





from django.db import models


def get_recommendation(request):
    user = request.user

    # Get all previous orders for the user
    previous_orders = Order.objects.filter(user=user)

    # Check if there are previous orders
    if previous_orders.exists():
        # Extract unique authors and categories from all previous orders
        all_authors = set()
        all_categories = set()

        for order in previous_orders:
            all_authors.update([book.authors.Author_name for book in order.books.all()])
            all_categories.update([book.categories.Cat_name for book in order.books.all()])

        # Extract unique books ordered in all previous orders
        ordered_books_in_all_orders = set()
        for order in previous_orders:
            ordered_books_in_all_orders.update(order.books.all())

        # Recommend books that have the same authors or categories as all previous orders, excluding ordered books
        recommended_books = Book.objects.filter(
            models.Q(authors__Author_name__in=all_authors) | models.Q(categories__Cat_name__in=all_categories)
        ).exclude(id__in=[book.id for book in ordered_books_in_all_orders])

        if recommended_books.exists():
            # Render the template with the recommended books
            return render(request, 'get_recommendation.html', {'recommended_books': recommended_books})
        else:
            return render(request, 'get_recommendation.html', {'message': "No recommended books found."})

    return render(request, 'get_recommendation.html', {'message': "No previous orders found."})