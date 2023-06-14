from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



# Create your models here.
class NewUser:
    email = models.EmailField()
    user_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    


time_choices = (
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
)


table_size_choices = (
    ("two_seater_window", "two_seater_window"),
    ("two_seater_corner", "two_seater_corner"),
    ("four_seater_window", "four_seater_window"),
    ("four_seater_middle", "four_seater_middle"),
    ("six_seater_corner", "six_seater_corner"),
    ("six_seater_window", "six_seater_window"),
    ("six_seater_middle", "six_seater_middle"),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name 
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField()
    start_time = models.CharField(choices=time_choices, default='18:00', max_length=100)
    party_size = models.CharField(choices=table_size_choices, max_length=100)
    extra_info = models.CharField(max_length=400)

    def __str__(self):
        return f'Booking for {self.party_size} at {self.restaurant} on {self.date}'