from . import views
from django.urls import path

app_name = "main"

urlpatterns=[
    path("", views.home_view, name="home_view"),
    path("properties/", views.prop_view, name="prop_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("dark_mode/", views.dark_mode, name="dark_mode"),
    path("light_mode/", views.light_mode, name="light_mode"),


]