from django.db import models

# Create your models here.

from apps.Juego.models import Juego
from apps.HistoriaClinica.models import HistoriaClinica

class Rutina(models.Model):
    
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    num_sesion = models.IntegerField(blank=True, null=True)
    preescripcion = models.CharField(max_length=300, blank=True, null=True)
    mano_derecha = models.BooleanField(blank=True, null=True)
    historiaClinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, blank=True, null=True)
