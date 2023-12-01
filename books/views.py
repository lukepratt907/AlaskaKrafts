from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("books:login_page"))
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
        return HttpResponseRedirect(reverse("books:home_page"))
    
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('books:home_page'))

def about_page(request):
    pass

def favorites_page(request):
    pass

def cart_page(request):
    pass

def favorite_view(request):
    pass