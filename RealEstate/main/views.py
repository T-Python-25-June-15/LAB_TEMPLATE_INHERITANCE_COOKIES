from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def properties_view(request: HttpRequest):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, "main/properties.html", {"properties": properties})

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')

def toggle_theme(request: HttpRequest):
    current_theme = request.COOKIES.get("theme", "light")
    new_theme = "dark" if current_theme == "light" else "light"
    response = HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("theme", new_theme, max_age=60*60*24)
    return response
