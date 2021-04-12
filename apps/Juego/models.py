from django.db import models


class Juego(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    description= models.CharField(max_length=300,blank=True, null=True)
   
   