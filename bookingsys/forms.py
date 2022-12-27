from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Restaurant


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    # start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    # end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
   
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
        
        

    # def clean_party_size(self):
    #     cleaned_party_size = self.cleaned_data["party_size"]
    #     all_booking = Booking.objects.all()
    #     for single_booking in all_booking:
    #         if single_booking.party_size 




