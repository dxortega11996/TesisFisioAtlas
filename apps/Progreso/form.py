from apps.Progreso.models import Progreso
from django import forms

class Progresoform(forms.ModelForm):
    class Meta:
        model=Progreso
        fields=[
            'gradoDolorInicial',
            'gradoDolorFinal',
            
            
        ]

        labels={
            'gradoDolorInicial':'Grado de Dolor Inicial',
            'gradoDolorFinal':'Gradode Dolor Final',
            
            
        }
        widgets={
            'gradoDolorInicial':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'gradoDolorFinal':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            
        }