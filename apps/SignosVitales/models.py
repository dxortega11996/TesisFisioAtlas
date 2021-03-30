from django.db import models

# Create your models here.
class SignosVitales(models.Model):
    peso = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    temperatura = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    talla = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    presion_arterial = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    imc = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    frec_respiratoria = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    frec_cardiaca = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    presion_arterial = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    
    
    
    