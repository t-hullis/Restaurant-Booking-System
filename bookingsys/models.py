from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



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
    start_time = models.TimeField()
    end_time = models.TimeField()
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])
    extra_info = models.CharField(max_length=400)

    def __str__(self):
        return f'Booking for {party} at {restaurant} on {date}'.format(party=self.party_size,
                                                                      restaurant=self.restaurant,
                                                                      date=self.date)




