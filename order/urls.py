# urls.py in the order app

from django.urls import path
from .views import create_order
from . import views
from .views import my_order_list
from django.conf import settings
from django.conf.urls.static import static
app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('my_orders/', my_order_list, name='my_order_list'),
    # Add more URLs as needed for order-related views
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)