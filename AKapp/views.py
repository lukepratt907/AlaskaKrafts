from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTaskForm
# Create your views here.

temp_accounts = {
    'Luke': '123',
}
def index(request):
    return render(request, "index.html")
    #return HttpResponse("Hello World!")

def register(request):
    if request.method == 'POST':
        f = NewTaskForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data["username"]
            password1 = f.cleaned_data["password1"]
            password2 = f.cleaned_data["passwords2"]
            if password1 == password2:
                if username not in temp_accounts:#not in database
                    #save all of it to the data base as an account
                    pass
                else:#username exists
                    return render(request, 'register.html', {
                        "form": f,
                        "errormessage": "username already exists"
                    })
            else:#passwords dont match
                return render(request, 'register.html', {
                    "form": f,
                    "errormessage": "Passwords must match"
                })
        else:#not valid
            return render(request, 'register.html', {"form": f})
    else:#not post
        return render(request, "register.html", {"form": NewTaskForm()})

def about(request):
    return render(request, "about.html")