
from django.shortcuts import render, redirect
from django.http import HttpRequest

properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]


def home_view(request: HttpRequest):
    return render(request, "main/home.html", {"properties": properties})


def properties_view(request: HttpRequest):
    return render(request, "main/properties.html", {"properties": properties})


def services_view(request: HttpRequest):
    return render(request, "main/services.html")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")


def contact_view(request: HttpRequest):
    return render(request, "main/contact.html")


def large_font_view(request: HttpRequest):
    response = redirect("main:home_view")
    response.set_cookie("font", "large", max_age=60 * 60 * 24)  # الكوكيز لمدة يوم
    return response


def normal_font_view(request: HttpRequest):
    response = redirect("main:home_view")
    response.delete_cookie("font")  # حذف الكوكيز
    return response
