from django.test import TestCase
from .models import Booking, Restaurant, User


class BookingsModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="toby", email="thulli@gmail.com", first_name="toby", last_name="hull", password="bitboi1818")
        # login = self.client.login(username='toby', password='bitboi1818')
        restaurant = Restaurant.objects.create(name="kfk", description="best food in town", opening_time="09:00", closing_time="22:00")
        Booking.objects.create(user=user, restaurant=restaurant, start_time="18:00", date="2022-11-16", party_size="two_seater_corner", extra_info="yes")

    def test_user_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    