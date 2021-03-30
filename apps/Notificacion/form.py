from apps.Profesional.models import Profesional
from django import forms
class Profesionalform(forms.ModelForm):
    class Meta:
        model=Profesional
        fields=[
            'nombre',
            'mensaje',
            
        ]
        labels={
            'nombre':'Nombre',
            'mensaje':'Mensaje',
            
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'mensaje':forms.TextInput(attrs={'class':'form-control', 'required':True }),
        }