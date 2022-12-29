from django.test import TestCase
from .forms import RegisterForm, BookingForm
from .models import User


class TestRegisterForm(TestCase):
   
    def test_register_form_requires_name(self):
        """
        tests in form can be passed with empty name field
        """
        form = RegisterForm({'user': ''})
        self.assertFalse(form.is_valid())
    
    def test_register_form_requires_email(self):
        """
        tests in form can be passed with empty email field
        """
        form = RegisterForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form_data= {
            'username': "mrtumnus",
            'email': "mrtum@gmail.com",
            'first_name': "Mr",
            'last_name': "Tumnus",
            'password1': "mrtumnus1818",
            'password2': "mrtumnus1818",
        }
        form = RegisterForm(data=form_data)
        
        self.assertEqual(form.fields['username'].label, "Username")
    




