from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, BookingForm, RestaurantForm
from django.contrib.auth.decorators import login_required, login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from .models import Booking, Restaurant
from django.contrib.auth.models import User


# Create your views here.
# @login_required(login_url="/login")
def home(request):
    return render(request, 'bookingsys/home.html')


@login_required(login_url="/login")
def bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    if request.method == "POST":
        booking_id = request.POST.get("booking-id")
        booking = Booking.objects.filter(id=booking_id)
        booking.delete()

    return render(request, 'bookingsys/bookings.html', {"bookings": bookings})

@login_required(login_url="login")
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('/bookings')
    else:
        form = BookingForm()

    return render(request, 'bookingsys/make_booking.html', {"form": form})


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="login")
def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.user = request.user
            restaurant.save()
            return redirect('/bookings')
    else:
        form = RestaurantForm()

    return render(request, 'bookingsys/add_restaurant.html', {"form": form})


def edit_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if booking.user.is_authenticated and booking.user == request.user:

        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                return redirect('/bookings')
        context = {'form': form}
        return render(request, 'bookingsys/edit_booking.html', {"form": form})
    else:
        return render(request, 'bookingsys/404.html')


def edit_restaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    form = RestaurantForm(instance=restaurant)

    if request.user.is_superuser:
        if request.method == 'POST':
            form = RestaurantForm(request.POST, instance=restaurant)
            if form.is_valid():
                restaurant = form.save(commit=False)
                restaurant.user = request.user
                restaurant.save()
                return redirect('/bookings')
        context = {'form': form}
        return render(request, 'bookingsys/edit_restaurant.html', {"form": form})
    else:
        return render(request, 'bookingsys/404.html')


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
    restaurants = Restaurant.objects.all()
    return render(request, 'bookingsys/restaurants.html', {"restaurants": restaurants})
        
