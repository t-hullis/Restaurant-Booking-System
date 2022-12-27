from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name="home"),
    path('sign-up', views.sign_up, name='sign_up'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('make-booking', views.make_booking, name='make_booking'),
    path('edit-booking/<str:pk>/', views.edit_booking, name='edit_booking'),
    path('bookings', views.bookings, name='bookings')
]