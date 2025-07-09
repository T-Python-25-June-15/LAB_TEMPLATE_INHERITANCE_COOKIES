from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_page(request: HttpRequest):
    return render(request, "home_page.html")

def properties_page(request:HttpRequest):

    properties = [
    {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
    {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
    {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
    {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request, "properties.html", context={"properties": properties})

def contact_page(request:HttpRequest):
    return render(request, "contact.html")



def dark_mood_view(request:HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mood", "dark")
    return response


def light_mood_view(request:HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mood", "light", max_age= - 3600)
    return response