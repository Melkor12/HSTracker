
from django.shortcuts import render

# Create your views here.

# reverse_lazy is used for resolving Django URL names into URL paths. 
# The resolution is not seen by the end user client as all of this work occurs 
# within the Django application code and framework code. We use reverse_lazy to 
# redirect the user to the login page upon successful registration.

# Import Django's template for User Creation Forms:
from django.contrib.auth.forms import UserCreationForm 
# Reverse_lazy  is used for resolving Django URL names into URL paths. 
# The resolution is not seen by the end user client as all of this work 
# occurs within the Django application code and framework code.
from django.urls import reverse_lazy
from django.views import generic

# Why use reverse_lazy instead of reverse I hope you're asking? The reason is 
# that for all generic class-based views the urls are not loaded when the file is imported, 
# so we have to use the lazy form of reverse to load them later when they're available.


# We're subclassing the generic class-based view CreateView in our SignUp class. We specify the use of 
# the built-in UserCreationForm and the not-yet-created template at signup.html. 
# And we use reverse_lazy to redirect the user to the login page upon successful registration.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm # This is a built in user creation form 
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
