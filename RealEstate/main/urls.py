from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),  
    path('properties/', views.properties_page, name='properties_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('theme/light/', views.to_light_change, name="light"),
    path('theme/dark/', views.to_dark_change, name="dark"),
]