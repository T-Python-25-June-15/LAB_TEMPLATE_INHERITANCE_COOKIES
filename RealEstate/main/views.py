from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def page_view(request: HttpRequest):
    r = render(request, 'main/homepage.html')
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

def contact_view(request: HttpResponse):
    r = render(request, 'main/contact.html')
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

def properties_view(request: HttpResponse):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    r = render(request, 'main/properties.html', {'properties': properties})
    if not 'mode' in request.COOKIES:
        r.set_cookie('mode', 'light', max_age=60*60*24*7)
    return r

from django.shortcuts import redirect
from django.http import HttpRequest

def change_mode(request: HttpRequest):
    current_url = request.META.get('HTTP_REFERER', '/') 
    r = redirect(current_url)
    
    if 'mode' in request.COOKIES:
        if request.COOKIES['mode'] == 'dark':
            r.set_cookie('mode', 'light')
        else:
            r.set_cookie('mode', 'dark')
    else:
        r.set_cookie('mode', 'light', max_age=60*60*24)

    return r
