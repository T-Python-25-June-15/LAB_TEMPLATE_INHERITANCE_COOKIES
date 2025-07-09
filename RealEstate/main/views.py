from django.shortcuts import render
from django.http import HttpResponse,HttpRequest


def home_page(request:HttpRequest):

    return render(request ,"main/index.html")
    