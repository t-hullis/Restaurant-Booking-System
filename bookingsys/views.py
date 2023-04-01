from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Booking, Restaurant


# Create your views here.
@login_required(login_url="/login")
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


def edit_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('/bookings')
    context = {'form': form}
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
    restaurants = Restaurant.objects.all()
    return render(request, 'bookingsys/restaurants.html', {"restaurants": restaurants})

        
