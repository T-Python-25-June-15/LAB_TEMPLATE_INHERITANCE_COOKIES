from . import views
from django.urls import path,include

app_name="main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('properties/', views.properties_view, name="properties_view"),
    path("darkmode/", views.dark_mode, name="dark_mode"),
    path("lightmode/", views.light_mode, name="light_mode"),
    path("contactus/", views.contactus, name="contactus"),

]