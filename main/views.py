from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index_view(request:HttpRequest):
    resp = render(request, 'main/index.html')
    if not 'mode' in request.COOKIES:
        resp.set_cookie('mode', 'light', max_age=60*60*24)
    return resp

def contact_view(request:HttpResponse):
    resp = render(request, 'main/contact.html')
    if not 'mode' in request.COOKIES:
        resp.set_cookie('mode', 'light', max_age=60*60*24)
    return resp

def properties_view(request:HttpResponse):
    resp = render(request, 'main/properties.html')
    if not 'mode' in request.COOKIES:
        resp.set_cookie('mode', 'light', max_age=60*60*24)
    return resp

def change_mode(request:HttpRequest):
    resp = redirect('/')
    if 'mode' in request.COOKIES:
        if request.COOKIES['mode'] == 'dark':
            resp.set_cookie('mode', 'light')
        else:
            resp.set_cookie('mode', 'dark')
        
    else:
        resp.set_cookie('mode', 'light', max_age=60*60*24)
        
    return resp
        
    