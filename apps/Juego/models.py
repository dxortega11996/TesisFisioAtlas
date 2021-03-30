from django.db import models


class Juego(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    