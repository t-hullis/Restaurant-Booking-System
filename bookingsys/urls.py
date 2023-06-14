from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name="home"),
    path('sign-up', views.sign_up, name='sign_up'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('make-booking', views.make_booking, name='make_booking'),
    path('edit-booking/<str:pk>/', views.edit_booking, name='edit_booking'),
    path('edit-restaurant/<str:pk>/', views.edit_restaurant, name='edit_restaurant'),
    path('bookings', views.bookings, name='bookings'),
    path('add-restaurant', views.add_restaurant, name='add_restaurant')
]