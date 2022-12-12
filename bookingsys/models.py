from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    


# Create your models here.

class User(models.Model):




# class Booking(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     full_name = models.CharField()
#     time = models.DateTimeField()
#     party_size = models.IntegerField()
#     resturaunt_id = models.Aggregate()

# class 