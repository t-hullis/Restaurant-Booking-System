from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewUser:
    email = models.EmailField()
    user_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    


# class Booking(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     # time = models.DateTimeField()

