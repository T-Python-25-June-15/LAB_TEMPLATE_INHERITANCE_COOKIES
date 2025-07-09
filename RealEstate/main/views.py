from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest


def home_page(request:HttpRequest):
    theme = request.COOKIES.get("theme", "light")
    return render(request ,"main/index.html", {"theme": theme})

def properties_page(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]

    theme = request.COOKIES.get("theme", "light")
    return render(request ,"main/properties.html", {"theme": theme,"properties": properties})

def contact_page(request:HttpRequest):
    theme = request.COOKIES.get("theme", "light")
    return render(request ,"main/contact.html", {"theme": theme})
    
def to_light_change(request:HttpRequest):

    response = redirect("/")
    response.set_cookie("theme","light",max_age=60*60*24)
    return response

def to_dark_change(request:HttpRequest):

    response = redirect("/")
    response.set_cookie("theme","dark",max_age=60*60*24)
    return response