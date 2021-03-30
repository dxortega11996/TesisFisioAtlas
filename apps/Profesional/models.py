from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profesional(models.Model):
    cedula = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento= models.DateField(null=True,blank=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='foto/', null=True,blank=True)
    autoidentificacion = models.CharField(max_length=30, blank=True, null=True)
    formacion = models.CharField(max_length=100, blank=True, null=True)
    codigoMSP = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    
    