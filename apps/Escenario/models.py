from django.db import models
from apps.Juego.models import Juego

# Create your models here.
class Escenario(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, blank=True, null=True)



