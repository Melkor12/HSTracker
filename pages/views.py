
from django.shortcuts import render, HttpResponse
# from .forms import InputForm

# Create your views here.

def index_view(request): # it is important that the word 'request' is writen here
    return render(request, template_name='home.html') # alternatively you can return a http response by typing: 'return HttpResponse('This is a Homepage')'

def about_view(request):
    return render (request, template_name= "about.html")

def contact_view(request):
    return render (request, template_name= "contact.html")

def dashboard_view(request):
    return render (request, template_name="dashboard.html")

def register_view(request):
    return render (request, template_name="registration/register.html")
