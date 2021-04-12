from django.conf.urls import url
from django.urls import path
from apps.Paciente.views import listarPaciente,RegistrarPaciente,ActualizarPaciente,EliminarPaciente,VisualHistoriaClinica,listarSeguimientoPaciente,activarHC,eliminarPacineteV2,RegistrarRutina,listarControlPaciente,actualizarSesion,finalizarRutina,listarReportes,visualizarReporte,visualizarGraficas
app_name='Paciente'

urlpatterns=[
    path('listarPaciente/',listarPaciente.as_view(), name="listarPaciente"),
    path('registrarPaciente/',RegistrarPaciente.as_view(), name="registrarPaciente"),
    path('actualizarPaciente/<int:pk>/',ActualizarPaciente.as_view(), name="actualizarPaciente"),
    path('eliminarPaciente/<int:pk>/',EliminarPaciente.as_view(), name="eliminarPaciente"),
    path('visualizarHCPaciente/<int:pk>/',VisualHistoriaClinica.as_view(), name="visualizarHCPaciente"),
    path('listarSeguimiento/',listarSeguimientoPaciente.as_view(), name="listarSeguimiento"),
    path('activarHistoriaClinica/',activarHC, name="activarHistoriaClinica"),
    path('eliminarPacineteV2/',eliminarPacineteV2, name="eliminarPacineteV2"),
    

    path('registrarRutina/<int:pk>/',RegistrarRutina.as_view(), name="registrarRutina"),
    path('listarControl/<int:pk>/',listarControlPaciente.as_view(), name="listarControl"),
    path('actualizarSesion/',actualizarSesion, name="actualizarSesion"),
    path('finalizarRutina/',finalizarRutina, name="finalizarRutina"),



    path('listarReportes/',listarReportes.as_view(), name="listarReportes"),
    path('visualizarReporte/<int:pk>/',visualizarReporte.as_view(), name="visualizarReporte"),
    path('visualizarGraficas/<int:pk>/',visualizarGraficas.as_view(), name="visualizarGraficas"),
        
]