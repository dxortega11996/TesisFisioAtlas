from django.db import models

# Create your models here.
class Notificacion(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    mensaje = models.CharField(max_length=100, blank=True, null=True)