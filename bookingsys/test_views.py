from django.test import TestCase


class TestViews(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bookingsys/home.html')
