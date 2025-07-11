from django.urls import path,include
from . import views as main 

app_name = 'main'

urlpatterns = [
    path('', main.page_view, name='page_view'),
    path('change_mode', main.change_mode, name='change_mode'),
    path('contact/', main.contact_view, name='contact_view'),
    path('properties/', main.properties_view, name='properties_view'),
]
