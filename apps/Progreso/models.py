from django.db import models
from apps.Juego.models import Juego
from apps.Control.models import Control
# Create your models here.
class Progreso(models.Model):
    gradoDolorInicial = models.IntegerField(blank=True, null=True)
    gradoDolorFinal = models.IntegerField(blank=True, null=True)
    control = models.OneToOneField(Control, on_delete=models.CASCADE, blank=True, null=True)
 