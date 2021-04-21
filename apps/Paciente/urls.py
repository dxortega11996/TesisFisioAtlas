from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.Paciente.views import listarPaciente,RegistrarPaciente,ActualizarPaciente,EliminarPaciente,VisualHistoriaClinica,listarSeguimientoPaciente,activarHC,eliminarPacineteV2,RegistrarRutina,listarControlPaciente,actualizarSesion,finalizarRutina,listarReportes,visualizarReporte,visualizarGraficas
app_name='Paciente'

urlpatterns=[
    path('listarPaciente/',login_required(listarPaciente.as_view()), name="listarPaciente"),
    path('registrarPaciente/',login_required(RegistrarPaciente.as_view()), name="registrarPaciente"),
    path('actualizarPaciente/<int:pk>/',login_required(ActualizarPaciente.as_view()), name="actualizarPaciente"),
    path('eliminarPaciente/<int:pk>/',login_required(EliminarPaciente.as_view()), name="eliminarPaciente"),
    path('visualizarHCPaciente/<int:pk>/',login_required(VisualHistoriaClinica.as_view()), name="visualizarHCPaciente"),
    path('listarSeguimiento/',login_required(listarSeguimientoPaciente.as_view()), name="listarSeguimiento"),
    path('activarHistoriaClinica/',activarHC, name="activarHistoriaClinica"),
    path('eliminarPacineteV2/',eliminarPacineteV2, name="eliminarPacineteV2"),
    

    path('registrarRutina/<int:pk>/',login_required(RegistrarRutina.as_view()), name="registrarRutina"),
    path('listarControl/<int:pk>/',login_required(listarControlPaciente.as_view()), name="listarControl"),
    path('actualizarSesion/',actualizarSesion, name="actualizarSesion"),
    path('finalizarRutina/',finalizarRutina, name="finalizarRutina"),



    path('listarReportes/',listarReportes.as_view(), name="listarReportes"),
    path('visualizarReporte/<int:pk>/',visualizarReporte.as_view(), name="visualizarReporte"),
    path('visualizarGraficas/<int:pk>/',visualizarGraficas.as_view(), name="visualizarGraficas"),
        
]