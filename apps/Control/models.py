from django.db import models
from apps.Rutina.models import Rutina
from apps.Juego.models import Juego


# Create your models here.

class Control(models.Model):
    fecha_visita = models.DateField(blank=True, null=True)
    valoracion = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)

    dolor = models.IntegerField( blank=True, null=True)
    rutina =models.ForeignKey(Rutina, on_delete=models.CASCADE, blank=True, null=True)
    numeroSesion = models.IntegerField( blank=True, null=True)
    juego =models.ForeignKey(Juego, on_delete=models.CASCADE, blank=True, null=True)
    orden = models.IntegerField( blank=True, null=True)