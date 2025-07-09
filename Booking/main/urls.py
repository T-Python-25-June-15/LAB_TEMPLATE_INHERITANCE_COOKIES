from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path ("" , views.home_view , name="home_view"),
    path ("properties/", views.properties_view, name="properties_view"),
    path ("contact/" , views.contact_view, name="contact_view"),
    path('set-mode/<str:mode>/', views.set_mode, name='set_mode'),
]

