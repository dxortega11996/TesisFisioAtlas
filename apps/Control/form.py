
from apps.Control.models import Control
from django import forms

class Controlform(forms.ModelForm):
    class Meta:
        model=Control
        fields=[
            'fecha_visita',
            'valoracion',
            'dolor',
        ]

        labels={
            'fecha_visita':'Fecha de visita',
            'valoracion':'Valoración,
            'dolor':'Grado de dolor',
        }
        widgets={
            'fecha_visita':forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'valoracion':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'dolor':forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }