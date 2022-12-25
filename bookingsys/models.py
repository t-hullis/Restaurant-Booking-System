from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


time_choices = (
    ("07:00", "07:00"),
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
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

class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    two_seaters = models.PositiveIntegerField()
    four_seaters = models.PositiveIntegerField()
    six_seaters = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField()
    start_time = models.CharField(choices=time_choices, default='18:00', max_length=12)
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])
    extra_info = models.CharField(max_length=400)

    def __str__(self):
        return f'Booking for {self.party_size} at {self.restaurant} on {self.date}'




