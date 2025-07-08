from django.urls import path
from . import views as main 

app_name = 'main'

urlpatterns = [
    path('', main.index_view, name='index_view'),
    path('change_mode', main.change_mode, name='change_mode'),
]
