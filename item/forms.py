# Utility Functions and Business Logic for Vending Machine Application
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import logging

from item.utils import is_password_strong
from item.views import render_login_error, login_view

logger = logging.getLogger('watchtower-logger')


def perform_authentication(request, details):
    """Authenticate a user based on provided details."""
    return authenticate(request, username=details['username'], password=details['password'])


def log_user_in(request, user):
    """Log a user into the system."""
    login(request, user)


def validate_registration_details(request):
    """Validate registration details and either create a user or return an error."""
    if request.method == 'POST':
        registration_details = extract_registration_details(request)
        validation_result = validate_details(registration_details)
        if validation_result['is_valid']:
            create_account(registration_details)
            return HttpResponseRedirect(reverse(login_view))
        else:
            context = {
                'registrationFailed': True,
                'error_message': validation_result['error_message']
            }
            return render(request, 'registration.html', context)
    return render(request, 'registration.html', {'registrationFailed': False})


def extract_registration_details(request):
    """Extract registration details from the request."""
    return {
        'username': request.POST.get('user'),
        'name': request.POST.get('name'),
        'last_name': request.POST.get('last_name'),
        'password': request.POST.get('password'),
        'confirm_password': request.POST.get('confirm_password')
    }


def validate_details(details):
    """Validate the provided registration details."""
    if User.objects.filter(username=details['username']).exists():
        return {'is_valid': False, 'error_message': "Username already exists."}
    elif details['password'] != details['confirm_password']:
        return {'is_valid': False, 'error_message': "Passwords do not match."}
    elif not is_password_strong(details['password']):
        return {'is_valid': False,
                'error_message': "Password must be at least 8 characters long and contain both numbers and letters."}
    return {'is_valid': True}


def create_account(details):
    """Create a new user with the provided details."""
    user = User(username=details['username'], first_name=details['name'], last_name=details['last_name'])
    user.set_password(details['password'])
    user.save()
    logger.info(f"User {user} has been registered")


def authenticate_user(request):
    """Authenticate a user and redirect to index or show an error on failure."""
    if request.method == 'POST':
        login_details = extract_login_details(request)
        user_authenticated = perform_authentication(request, login_details)
        username = request.POST.get('user')
        if user_authenticated:
            log_user_in(request, user_authenticated)
            logger.info(f"User {username} logged in")
            return HttpResponseRedirect(reverse('index'))
        else:
            logger.warning(f"User {username} has attempted to login  with invalid details.")
            return render_login_error(request)
    return render(request, 'login.html')


def extract_login_details(request):
    """Extract login details from the request."""
    return {
        'username': request.POST.get('user'),
        'password': request.POST.get('password')
    }
