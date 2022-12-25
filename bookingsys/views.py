from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello!")

@login_required(login_url="/login")
def home(request):
    return render(request, 'bookingsys/home.html')


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def restaurants(request):
    return render(request, 'bookingsys/restaurants.html')

        
