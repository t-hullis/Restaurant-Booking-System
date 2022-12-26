from django.test import TestCase
from .models import Booking

# Create your tests here.
all_bookings = Booking.objects.all()
for single_booking in all_bookings:
    print(single_booking.date)