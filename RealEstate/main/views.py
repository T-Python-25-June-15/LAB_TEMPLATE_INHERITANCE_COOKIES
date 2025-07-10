from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def page_view(request:HttpRequest):
    r = render(request, 'main/homepage.html')
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

def contact_view(request:HttpResponse):
    r = render(request, 'main/contact.html')
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

def properties_view(request:HttpResponse):
    r = render(request, 'main/properties.html')
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

def change_mode(request:HttpRequest):
    r = redirect('/')
    if 'mode' in request.COOKIES:
        if request.COOKIES['mode'] == 'dark':
            r.set_cookie('mode', 'light')
        else:
            r.set_cookie('mode', 'dark')
        
    else:
        r.set_cookie('mode', 'light', max_age=60*60*24)
        
    return r
        
    