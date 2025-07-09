from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('properties/',views.properties_view,name="properties_view"),
    path('contact/us/',views.contact,name="contact"),
    path('set/theme/', views.set_theme, name='set_theme'),
    
]