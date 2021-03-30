from django.db import models
from apps.Provincia.models import Provincia
from apps.Canton.models import Canton
from apps.Profesional.models import Profesional
# Create your models here.
from django.contrib.auth.models import User

class Paciente(models.Model):
    vDependiente=( 
        ('SI','SI'),
        ('NO','NO')
    )
    cedula = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    fechaCita= models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    historiaClinica= models.CharField(max_length=100,choices=vDependiente,blank=True, null=True)
    seguimiento= models.CharField(max_length=100,choices=vDependiente,blank=True, null=True)
    patologia= models.CharField(max_length=300,blank=True, null=True)
    profesional=models.ForeignKey(Profesional, on_delete=models.CASCADE, blank=True, null=True)