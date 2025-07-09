from . import views
from  django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home_view,name="home"),
    path('properties/',views.properties_view,name="properties"),
    path('contact/',views.contact_view,name="contact"),
    path('dark-mode/', views.enable_dark_mode, name="enable_dark_mode"),
    path('light-mode/', views.disable_dark_mode, name="disable_dark_mode"),

]
