from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Restaurant, Booking
from .forms import RegisterForm, BookingForm, RestaurantForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpass')
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant', description='Test Description',
            opening_time='12:00', closing_time='22:00')
        self.booking = Booking.objects.create(
            user=self.user, restaurant=self.restaurant, date='2023-04-07',
            start_time='18:00', party_size='two_seater_window', extra_info='Test Info')

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/home.html')

    def test_bookings_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('bookings')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/bookings.html')

    def test_make_booking_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('make_booking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/make_booking.html')

    def test_edit_booking_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('edit_booking', args=[self.booking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/make_booking.html')

    def test_sign_up_view(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

    def test_restaurants_view(self):
        url = reverse('restaurants')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/restaurants.html')
