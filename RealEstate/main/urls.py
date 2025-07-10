from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("properties/", views.properties_view, name="properties"),
    path("contact/", views.contact_view, name="contact"),
    path("dark/mode/", views.dark_mode_view, name="dark_mode_view"),
    path("light/mode/", views.light_mode_view, name="light_mode_view"),
]