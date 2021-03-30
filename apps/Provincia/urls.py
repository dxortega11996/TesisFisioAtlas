from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.Provincia.views import buscarCantones

app_name='Provincia'

urlpatterns=[
  
    
    path('buscarCantones/',buscarCantones, name="buscarCantones"),     
]