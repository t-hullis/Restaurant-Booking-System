from django.contrib import admin
from .models import *
# from django.contrib 

# Register your models here.
admin.site.site_header = "Eateasy"
admin.site.register(Booking)
admin.site.register(Restaurant)