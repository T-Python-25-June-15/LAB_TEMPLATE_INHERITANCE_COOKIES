from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]

# render is used to connect views with html templates, it loads the the temp
# Create your views here.

def home_view(request : HttpRequest):
    return render(request, "main/home.html")

def properties_view(request : HttpRequest):
    return render(request, 'main/properties.html', {"properties": properties})

def contact(request):
    return render(request, 'main/contactus.html')

def set_theme(request):
    theme = request.GET.get('theme', 'light')
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', theme)
    return response
