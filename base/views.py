# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


from django.http import HttpResponse
from django.contrib.auth import authenticate,login 
from Book.models import Book
from django.contrib.auth.models import User ,auth
from django.contrib import messages




def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about_us.html')

def featured(request):
    return render(request, 'featured_books.html')

def arrivals(request):
    return render(request, 'arrival.html')

def reviews(request):
    return render(request, 'reviews.html')

def login(request):
    return render(request, 'login.html')


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('home')
#     else:
#         form = RegistrationForm()

#     return render(request, 'registration.html', {'form': form})



def search_books(request):
    search_query = request.GET.get('q', '')
    found_books = Book.objects.filter(title__icontains=search_query)

    context = {'found_books': found_books, 'search_query': search_query}
    return render(request, 'search_results.html', context)



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(email = email).exists():
                messages.info(request , 'Email Taken Already')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request ,'Username Taken Already')
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username , email= email , password= password)
                user.save()
                login_user = auth.authenticate(request , username = username , password = password)
                auth.login(request , login_user)
                return redirect('home')
        else:
            messages.info(request , "Password Not Matched")
            return redirect ('register')
    else:
        return render(request , 'registration.html')
    


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            return redirect('home')
        else:
            messages.info(request , 'Credentials Invalid')
            return redirect('login')
    return render(request , 'login.html')