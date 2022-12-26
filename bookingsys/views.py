from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Booking

# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request, 'bookingsys/home.html')


def bookings(request):
    return render(request, 'bookingsys/bookings.html')


@login_required(login_url="login")
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("/home")
    else:
        form = BookingForm()

    return render(request, 'bookingsys/make_booking.html', {"form": form})


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

        
