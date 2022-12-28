from django.test import TestCase
from .forms import RegisterForm, BookingForm


class TestRegisterForm(TestCase):
    def test_register_form_requires_name(self):
        form = RegisterForm({'user': ''})
        self.assertFalse(form.is_valid())



