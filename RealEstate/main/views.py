from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

def home_view(request):
    mode = request.COOKIES.get('mode', 'light')
    return render(request, 'main/home.html', {'mode': mode})

def properties_view(request: HttpRequest):
    mode = request.COOKIES.get('mode', 'light')
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    context = {
        'properties': properties,
        'mode': mode,
    }

    return render(request, 'main/properties.html', context)

def contact_view(request: HttpRequest):
    mode = request.COOKIES.get('mode', 'light')
    return render(request, "main/contact.html",{'mode': mode})
def dark_mode_view(request):
    next_url = request.GET.get('next', 'main:home')
    response = redirect(next_url)
    response.set_cookie('mode', 'dark', max_age=60*60*24*30)
    return response

def light_mode_view(request):
    next_url = request.GET.get('next', 'main:home')
    response = redirect(next_url)
    response.set_cookie('mode', 'light', max_age=60*60*24*30)
    return response