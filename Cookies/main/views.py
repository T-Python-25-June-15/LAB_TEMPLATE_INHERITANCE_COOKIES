from django.shortcuts import render ,redirect
from django.http import HttpRequest,response
# Create your views here.

def home_view(request):

    return render(request,"main/home.html")

def properties_view(request):

    return render(request,"main/properties.html")

def contact_view(request):
    
    return render(request,"main/contact.html")

def enable_dark_mode(request):
    response = redirect("main:home")
    response.set_cookie("darkMode", "on", max_age=60*60*24*30)
    return response

def disable_dark_mode(request):
    response = redirect("main:home")
    response.set_cookie("darkMode", "off", max_age=60*60*24*30)
    return response