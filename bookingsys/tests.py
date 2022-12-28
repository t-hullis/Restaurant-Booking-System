# from django.test import TestCase, Client
# from .models import Booking, Restaurant


# class ClientTest(TestCase):

#     def test_homepage(self):
     
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, 'bookingsys/home.html')

#     def test_restaurant_page(self):
    
#         response = self.client.get('/restaurants')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bookingsys/restaurants.html')

#     def test_bookings_page(self):
    
#         response = self.client.get('/bookings')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bookingsys/bookings.html')
