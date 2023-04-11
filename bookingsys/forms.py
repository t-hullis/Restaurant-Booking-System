from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Restaurant


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="someone@example.com")
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class BookingForm(forms.ModelForm):
    date = forms.DateField(help_text="YYYY-MM-DD",widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    extra_info = forms.CharField(required=False)
    
    class Meta:
        model = Booking
        fields = ["restaurant", "date", "start_time",  "party_size", "extra_info"]
    
    def clean(self):
        cleaned_restaurant = self.cleaned_data["restaurant"]
        cleaned_date = self.cleaned_data["date"]
        cleaned_start_time = self.cleaned_data["start_time"]
        cleaned_party_size = self.cleaned_data["party_size"]
        all_booking = Booking.objects.all()

        for single_booking in all_booking:
            if single_booking.date == cleaned_date and single_booking.start_time == cleaned_start_time and single_booking.restaurant == cleaned_restaurant and single_booking.party_size == cleaned_party_size:
                raise forms.ValidationError("Already booked, please try a different time or date.")
            # if single_booking.start_time < 


class RestaurantForm(forms.ModelForm): 
    
    class Meta:
        model = Restaurant
        fields = ["name", "description", "opening_time",  "closing_time"]
    
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    opening_time = forms.TimeField()
    closing_time = forms.TimeField()

