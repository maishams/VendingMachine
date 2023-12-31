from django.urls import path
from . import views

urlpatterns = [
    # Main page displaying all items.
    path('', views.index, name='index'),

    # Payment page for a specific item type.
    path('<int:itemId>/payment/', views.payment, name='payment'),

    # Endpoint to process payment for a specific item type.
    path('<int:itemId>/payment/pay/', views.pay, name='pay'),

    # About page of the website.
    path('about/', views.about, name='about'),

    # Contact page of the website.
    path('contact/', views.contact, name='contact'),

    # User registration page.
    path('registration/', views.registration, name='registration'),

    # Endpoint to validate user registration details.
    path('registration/validateUser', views.validateRegistrationDetails, name='validateUser'),

    # User login page.
    path('login/', views.loginView, name='log'),

    # Endpoint to authenticate user login details.
    path('login/authenticate/', views.authenticateUser, name='authenticate'),

    # Endpoint to log out the authenticated user.
    path('logout/', views.logoutView, name='logout'),

    # User account page displaying purchase history and other details.
    path('account/', views.account, name='account'),

    # Endpoint to clear the user's purchase history.
    path('account/clean', views.cleanHistory, name='cleanHistory'),
]
