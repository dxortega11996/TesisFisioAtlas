from apps.Progreso.models import Progreso
from django import forms

class Progresoform(forms.ModelForm):
    class Meta:
        model=Progreso
        fields=[
            'tiempo_realizado',
            'fecha_realizado',
            'dolor',
            
        ]

        labels={
            'tiempo_realizado':'Tiempo realizado',
            'fecha_realizado':'Fecha de realización',
            'dolor':'Dolor',
            
        }
        widgets={
            'tiempo_realizado':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'fecha_realizado':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'dolor':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            
        }