from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name="home"),
    path('properties/', views.properties_page, name="properties"),
    path('contact/', views.contact_page, name="contact"),
    path('theme/light/', views.to_light_change, name="light"),
    path('theme/dark/', views.to_dark_change, name="dark"),
    
]
