from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.Profesional.views import ActualizarProfesional,RegistrarProfesional,listarProfesional,actualizarEstado
app_name='Profesional'

urlpatterns=[
  
    path('registrarProfesional/',RegistrarProfesional.as_view(), name="registrarProfesional"),
    path('actualizarProfesional/<int:pk>/',ActualizarProfesional.as_view(), name="actualizarProfesional"),
    path('listarProfesional/',listarProfesional.as_view(), name="listarProfesional"),  
    path('actualizarestado/',actualizarEstado, name="actualizarestado"),     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)