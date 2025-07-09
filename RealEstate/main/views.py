from django.http import HttpRequest
from django.shortcuts import render, redirect

def home_view(request: HttpRequest):
    darkmode = request.COOKIES.get('darkmode', 'false')
    response = render(request, "main/homepage.html", {"darkmode": darkmode})
    return response

def prop_view(request: HttpRequest):
    properties = [
        {"title": "VILLA MODERN IN MALQA", "image": "villa1.jpg"},
        {"title": "GREAT HOME FOR YOU IN RIMAL", "image": "villa2.jpg"},
        {"title": "VILLA WITH 8 BEDROOMS IN SWEDEY", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    darkmode = request.COOKIES.get('darkmode', 'false')
    return render(request, "main/properties.html", {"properties": properties, "darkmode": darkmode})

def contact_view(request: HttpRequest):
    darkmode = request.COOKIES.get('darkmode', 'false')
    response = render(request, "main/contact.html", {"darkmode": darkmode})
    return response

def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('darkmode', 'true', max_age=60*60*24)
    return response

def light_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('darkmode', 'false', max_age=60*60*24)
    return response