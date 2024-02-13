from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from .models import Book 
from django.contrib.auth import logout 
from django.db.models import Q
from .models import Book




class BookDetailViewWithSimilarBooks(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Assuming authors and categories are ForeignKeys in the Book model
        similar_books = Book.objects.filter(
            Q(authors=self.object.authors) | Q(categories=self.object.categories)
        ).exclude(id=self.object.id).distinct()[:5]

        context['similar_books'] = similar_books
        return context

def new_arrival(request):
    

    arrival_books = Book.objects.order_by('-publication_date')[:10]  
    context = {'arrival_books': arrival_books}
    return render(request, 'arrival.html', context)

def featured_books(request):
    featured_books = Book.objects.all()[:7] 
    return render(request, 'featured_books.html', {'featured_books': featured_books})


def search_books(request):
    search_query = request.GET.get('search_query', '')
    found_books = Book.objects.filter(title__icontains=search_query)

    context = {'found_books': found_books, 'search_query': search_query}
    return render(request, 'search_results.html', context)




def custom_logout(request):
    logout(request)
    return redirect('home') 
  


