from django.db import models
from apps.Provincia.models import Provincia
# Create your models here.
class Canton(models.Model):
    nombre=models.CharField(max_length=50)
    provincia=models.ForeignKey(Provincia,null=True, blank=True, on_delete=models.CASCADE)
