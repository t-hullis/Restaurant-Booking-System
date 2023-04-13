# Restaurant Booking System

Bookingsys is a python django web app for making resservations at restaurants.

![this is an image to show resposiveness](static/images/computerscrren.png)
![this is an image to show resposiveness](static/images/ipadscreen.png)
![this is an image to show resposiveness](static/images/iphonescreen.png)

## Abstract
This project was designed to streamline the booking procces for a chain of restaurants. All a users bookings can be seen in one place, with the capablity to create, read, edit and delete all the bookings. A user can only CRUD thier own bookings with no way of seeing other users bookings. The idea was to create a deliveroo style app but instead of making food orders, you simply can book seats.

## User Stories

**User Story [#3](https://github.com/t-hullis/Restaurant-Booking-System/issues/3):** 
As a customer, I can add a booking for a meal in a specific restaurant at a specific date/time, for a specific number of people

 **User Story [#2](https://github.com/t-hullis/Restaurant-Booking-System/issues/2):** As a site user I can select the date, time, party size and allergies so that I can customize the booking to suit my needs

 **User Story [#4](https://github.com/t-hullis/Restaurant-Booking-System/issues/4):** As a site user i can manage my booking so that reservations can be canceled, time/numbers can be changed

 **User Story [#5](https://github.com/t-hullis/Restaurant-Booking-System/issues/5):** As a Site user i can add an account for the website so that booking process is streamlined and can identify users

 **User Story [#6](https://github.com/t-hullis/Restaurant-Booking-System/issues/6):** As a restaurant owner/manager i can create a specific restaurant account so that my restaurant info can be displayed and integrated into the app, for users to use

 **User Story [#8](https://github.com/t-hullis/Restaurant-Booking-System/issues/8):** As a site user i can view a page or card/widget about each restaurant so that users can get information like location, opening hours, dietary requirements, etc ..

 **User Story [#10](https://github.com/t-hullis/Restaurant-Booking-System/issues/10):** As a user i can not double book a table in a restaurant so that i can be sure to get a table when i book one

 **User Story [#11](https://github.com/t-hullis/Restaurant-Booking-System/issues/11):** As a user i can view all my bookings so that it is easy to view and manage my bookings



# UX

## User
- Nav Bar : The nav bar spans all of the pages of this website and allows you to got to the restaurant page and bookings page easily. It also has a button on right, which depending on the login status of the user, will change from login to logout.
![homepage](static/images/readmemd/homepage.png)

- Home page : The front end of this website is very simple. The text is ment to grab the users atention then move them straight through to the booking page with minimal distraction.  
![homepage](static/images/readmemd/homepage.png)
- Design : 
![homepage](static/images/readmemd/designhome.png)

- Restaurant page : The user is met by cards diplaying the current restaurants you are able to book on the app. Links to Bookings page can be found. The cards diplay the name of the restaurant, a desription, as well was their opening times and closing times.
![restaurant](static/images/readmemd/restaurantpage.png)
- Design : 
![restaurant](static/images/readmemd/designrestaurants.png)

- Bookings page :  This page has a similar set up to to the restaurants page but it has the added functionality of the user being able to update/edit and delete bookings which belong to them.
![booking](static/images/readmemd/bookingpage.png)
- Design :
![homepage](static/images/readmemd/designbooking.png)

- Forms : For the forms i have used the cripsy forms library. This streamlined the form making process and added in error handling. 
![forms](static/images/readmemd/createaccountform.png)
![forms](static/images/readmemd/loginform.png)
![forms](static/images/readmemd/editbookingform.png)
- Design :
![homepage](static/images/readmemd/designlogin.png)

## Admin

-  The superuser (restaurant owner/manager) can add new retaurants to the database specifying restaurant detailsin the page that is link added to the nav bar, only avaible to the superuser, which takes them to a page form where they can add a new restuarant to the website for costomers to book.
![admin](static/images/readmemd/superuseradd.png)
![admin](static/images/readmemd/superuserdisp.png)

- The admin can also access the conrol panel for where he/she can manage restaurants and bookings directly. All CRUD functions for the project can be accessed from here. 
![admin](static/images/readmemd/adminpage1.png)

## Autherisation
In order to access your bookings, text decorators have been used, so you have to be logged in. This can be seen in views.py. The booking view stops other users from being able to see your bookings by onoly showing the booking with the same user id as current user.

## Databases
![this is an image of the models code](static/images/databaseimage.png)

All my databases have been created using django and postgres. 

- Restaurants : This is a model for the data of the restaurants. it holds opening times, closing times as well as a description and the name. This data can be diplayed.

- Bookings : Specifies booking start time, party size and extra info. It also has two forign keys which link it to the user model as well as Restruant models, so the bookings can be specifed to an exact restaurant.


# Testing

- testing has been done to make sure invalid forms are rejected, all tests pass

- testing has been done to make sure correct form secontions are running in form

# Deployment
## Technologies Used
 
This project has been deoplyed on heroku.

- [Django](https://www.djangoproject.com/)
    -  Framework used to build the project.
- [Python](https://www.python.org/)
- [Bootstrap](https://getbootstrap.com/)
    - Makes mobile first responsive design.
- [GitHub](https://github.com/)
    - Holds and stores project.
- [Gitpod](https://www.gitpod.io/)
    - Development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - App deployed here.
- Crispy forms

# Bugs
- The form to update a booking wouldnt pre load exsiting data into it. this was solved by adding an edit view into views.py and taking instance data.

- 

