"""HStracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #"include" statement imports other modules and their Urls

# imports different views from other Apps. 
# if you do not import the right view then you will not be able to connect paths to them !!!!!!
# in this case you are importing from the app pages (pages.views file)
# if you would want to import from accounts you would import from accounts.views
from pages.views import index_view, about_view, contact_view, dashboard_view # forms_view

# 'Urlpatterns' connects the Imported Views to Paths 
urlpatterns = [
    #'admin.site.urls' defines the path to the admin page of the website
    path('admin/', admin.site.urls), 
    # '' means this is the root path of the website
    path('', index_view, name = 'index'),
    # A project-level url for the accounts app-MUST BE INCLUDED above our included Django auth app.
    # Django will look top to bottom for Url Patterns so when it sees a Url Route within our accounts app that matches one in the built-in auth app, it will choose the Accounts Route first. 
    #!!!!! THIS  POINTS TO THE ACCOUNTS APP THAT YOU'VE CREATED!!!!
    path('accounts/', include('accounts.urls')),
    # Add Django site authentication urls (for login, logout, password management)
    # In other words this adds the URL mapping for the following URLs:
    #accounts/ login/ [name='login']
    #accounts/ logout/ [name='logout']
    #accounts/ password_change/ [name='password_change']
    #accounts/ password_change/done/ [name='password_change_done']
    #accounts/ password_reset/ [name='password_reset']
    #accounts/ password_reset/done/ [name='password_reset_done']
    #accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #accounts/ reset/done/ [name='password_reset_complete']
    # !!!!!! Just add the HTML files to the Templates/Registration Folder 
    # and all of the URLs will be available !!!!!!
    # Those Django.contrib.auth.urls are urls itself. meaning that when you include them, 
    # it automatically includes some built in django urls for example, login, sign up, password reset,
    #  password reset confirmation, etc. They are useful if you do not want to do coding on your own, 
    # meaning creating your own views !!!!!!!
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name = 'contact'),
    path('dashboard/', dashboard_view, name = 'dashboard'),
    # path('forms/', forms_view, name = 'forms'),
   ]
