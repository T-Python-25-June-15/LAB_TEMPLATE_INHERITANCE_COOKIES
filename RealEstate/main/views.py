from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest) -> HttpResponse:
    response = render(request, 'main/index.html')
    return response


def dark_mode_view(request: HttpRequest) -> HttpResponse:
    redirect_url = request.META.get('HTTP_REFERER', 'main:home_view')
    response = redirect(redirect_url)
    response.set_cookie('mode', 'dark', max_age=60*60*24*7)
    return response

def light_mode_view(request: HttpRequest):
    redirect_url = request.META.get('HTTP_REFERER', 'main:home_view')
    response = redirect(redirect_url)
    response.delete_cookie('mode')
    return response


def properties_view(request: HttpRequest) -> HttpResponse:
    properties = [
    {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
    {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
    {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
    {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    response = render(request, 'main/properties.html', context={'properties':properties})
    return response 


def contact_view(request: HttpRequest) -> HttpResponse:
    response = render(request, 'main/contact.html')
    return response