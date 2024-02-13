from django.urls import path
from . import views
from .views import search_books


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about, name="about"),
    path('featured/',views.featured, name="featured"),
    path('arrivals/',views.arrivals, name="arrivals"),
    path('reviews/',views.reviews, name="reviews"),
    path('login/',views.signin, name="login"),
    path('register/',views.signup, name="register"),
    path('search/',search_books, name='search_results'),
    
   
     
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)