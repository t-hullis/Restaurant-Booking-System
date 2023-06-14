from django.urls import reverse, resolve
from django.test import TestCase

from .views import home, bookings, make_booking, add_restaurant, edit_booking, sign_up, restaurants


class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_bookings_url_resolves(self):
        url = reverse('bookings')
        self.assertEqual(resolve(url).func, bookings)

    def test_make_booking_url_resolves(self):
        url = reverse('make_booking')
        self.assertEqual(resolve(url).func, make_booking)

    def test_add_restaurant_url_resolves(self):
        url = reverse('add_restaurant')
        self.assertEqual(resolve(url).func, add_restaurant)

    def test_edit_booking_url_resolves(self):
        url = reverse('edit_booking', args=[1])
        self.assertEqual(resolve(url).func, edit_booking)

    def test_sign_up_url_resolves(self):
        url = reverse('sign_up')
        self.assertEqual(resolve(url).func, sign_up)

    def test_restaurants_url_resolves(self):
        url = reverse('restaurants')
        self.assertEqual(resolve(url).func, restaurants)
