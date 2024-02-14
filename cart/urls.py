# urls.py in your cart app

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart, view_cart, remove_from_cart, update_quantity

urlpatterns = [
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('view/', view_cart, name='view_cart'),
    path('remove/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:book_id>/', update_quantity, name='update_quantity'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
