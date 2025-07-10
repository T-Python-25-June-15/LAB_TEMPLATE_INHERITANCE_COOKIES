from django.urls import path
from . import views as main 

app_name = 'main'

urlpatterns = [
    path('', main.index_view, name='index_view'),
    path('change_mode', main.change_mode, name='change_mode'),
    path('contact/', main.contact_view, name='contact_view'),
    path('properties/', main.properties_view, name='properties_view'),
]
