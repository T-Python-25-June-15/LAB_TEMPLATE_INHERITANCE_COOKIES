from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request: HttpRequest):

    return render(request, "main/index.html")

def properties_view(request: HttpRequest):

    return render(request, "main/properties.html")

def contact_view(request: HttpRequest):

    return render(request, "main/contact.html")
