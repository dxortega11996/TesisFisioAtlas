from django.urls import path
from . import views

from apps.inicio.views import inicio,new

app_name='Inicio'
urlpatterns = [
    
    path('',inicio, name="inicio"),
    path(r'new/', new, name="new"),
]