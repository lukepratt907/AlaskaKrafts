from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from .models import User, Book
from .forms import Pic

# Create your views here.
def home_page(request):
    if request.user.is_anonymous != True:
       return render(request, 'index.html', {
        'books': Book.objects.all(),
        'user': request.user,
        'cart': request.user.cart.all(), # add this when user is logged in
        'favorites': request.user.favorites.all() # add this when user is logged in
        })
    else: 
        return render(request, 'index.html', {
            'books': Book.objects.all(),
            'user': request.user,
            #'cart': request.user.cart.all(), # add this when user is logged in
            #'favorites': request.user.favorites.all() # add this when user is logged in
        })

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home-page"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })

    else:
        return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.htmk", {
                'message': "Passwords do not match"
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'register.html', {
                'message': 'username already exists'
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home-page"))
    
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home-page'))

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

@login_required(login_url='login.html')
def favorites_page(request):
    return render(request, 'favorites.html', {
        'favorites': request.user.favorites.all()
    })

@login_required(login_url='login.html')
def cart_page(request):
    return render(request, 'cart.html', {
        'cart': request.user.cart.all()
    })

@login_required(login_url='login.html')
def cart_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.cart.add(book)
    request.user.save()
    status = {
        'id': book_id
    }
    return redirect("cart-page")
    return JsonResponse(status)

@login_required(login_url='login.html')
def removecart_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.favorites.remove(book)
    request.user.save()
    status = {
        'id': book_id
    }
    return redirect("cart-page")
    return JsonResponse(status)

@login_required(login_url='login.html')
def favorite_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.favorites.add(book)
    request.user.save()
    status = {
        'id': book_id
    }
    return JsonResponse(status)

@login_required(login_url='login.html')
def removefavorite_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.favorites.remove(book)
    request.user.save()
    status = {
        'id': book_id
    }
    return JsonResponse(status)

def profile_page(request):
    return render(request, 'profile.html', {
        'user': request.user,
    })

def editpic(request):
    if request.method == 'POST':
        form = Pic(request.POST)
        if form.is_valid():
            pic = form.save()
            pic.save()
            return redirect("profile-page")
        else:
            return redirect("home-page")
    else:
        return render(request, 'editpic.html', {
            'form': Pic
        })

from django.db.models import Q
def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        books = Book.objects.all()

    return render(request, 'search.html', {'books': books, 'query': query})
