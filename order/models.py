# models.py in the order app

from django.db import models
from django.contrib.auth.models import User
from Book.models import Book

PAYMENT_OPTIONS = [
    ('cod', 'Cash on Delivery'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Add this line
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    payment_option = models.CharField(max_length=50, choices=PAYMENT_OPTIONS,default='cod')
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} - {self.user.username}"
