from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home_view (request:HttpRequest):
    return render(request , "main/index.html")

def set_mode(request: HttpRequest, mode: str):
    if mode not in ['light', 'dark']:
        mode = 'light'
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', mode, max_age=60*60*24*30)
    return response

def properties_view (request:HttpRequest):
    return render (request, "main/properties.html")

def contact_view (request:HttpRequest):
    return render (request, "main/contact.html")


