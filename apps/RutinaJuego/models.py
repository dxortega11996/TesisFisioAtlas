from django.db import models
from apps.Juego.models import Juego
from apps.Rutina.models import Rutina
# Create your models here.
class RutinaJuego(models.Model):
    rutina =models.ForeignKey(Rutina, on_delete=models.CASCADE, blank=True, null=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, blank=True, null=True)
    
    

