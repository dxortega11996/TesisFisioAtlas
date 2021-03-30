from django.db import models
from apps.Control.models import Control

# Create your models here.
class Intento(models.Model):
    
    puntaje = models.IntegerField( blank=True, null=True)
    tiempo = models.CharField(max_length=20,blank=True, null=True)
    fechaHora = models.DateTimeField(blank=True, null=True)
    tipoJuego=models.CharField(max_length=20,blank=True, null=True)
    dificultad=models.CharField(max_length=20,blank=True, null=True)
    control = models.ForeignKey(Control, on_delete=models.CASCADE, blank=True, null=True)
    