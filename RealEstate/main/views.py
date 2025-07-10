from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]

def home_view(request: HttpRequest):
    return render(request, "main/home.html")

def properties_view(request: HttpRequest):
    return render(request, "main/properties.html", {"properties": properties})

def contact_view(request: HttpRequest):
    return render(request, "main/contact.html")

def set_dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie("theme", "dark", max_age=60*60*24*30) #add cookie
    return response

def set_light_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie("theme", "dark", max_age=-3600)  # remove cookie
    return response
