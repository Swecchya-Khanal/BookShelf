from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_logout
from .views import BookDetailViewWithSimilarBooks
urlpatterns = [
    path('featured/', featured_books, name='featured_books'),
    path('search/', search_books, name='search_books'),
    path('book/<int:pk>/', BookDetailViewWithSimilarBooks.as_view(), name='book_detail'),
    path('new_arrival/', new_arrival, name='new_arrival'),
    path('logout/', custom_logout, name='logout'),
    path('browse/', browse_books, name='browse_books'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)