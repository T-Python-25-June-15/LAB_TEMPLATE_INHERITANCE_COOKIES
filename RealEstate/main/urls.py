from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('properties/', views.properties_page, name= 'properties_page'),
    path('contact/', views.contact_page, name= 'contact_page'),
    path('dark/mood/', views.dark_mood_view, name= 'dark_mood_view'),
    path('light/mood/', views.light_mood_view, name= 'light_mood_view'),
]