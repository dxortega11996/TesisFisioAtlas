from django.contrib.auth.models import User
from apps.Rutina.models import Rutina
from django import forms

class Rutinaform(forms.ModelForm):
    class Meta:
        model=Rutina
        fields=[
            'fecha_inicio',
            'fecha_fin',
            'num_sesion',
            'preescripcion',
            'mano_derecha',
            'historiaClinica',
        ]

        labels={
            'fecha_inicio':'Fecha de inicio',
            'fecha_fin':'Fecha de fin',
            'num_sesion':'Numero de sesion',
            'preescripcion':'Prescripción',
            'mano_derecha':'Mano derecha',
            'historiaClinica':'historiaClinica',
        }
        widgets={
            'fecha_inicio':forms.TextInput(attrs={'class': 'form-control datepicker tamanio', 'type': 'date' }),
            'fecha_fin':forms.TextInput(attrs={'class': 'form-control datepicker tamanio', 'type': 'date' }),
            'num_sesion':forms.TextInput(attrs={'class':'form-control tamanio', 'type': 'number','requiered':True }),
            'preescripcion':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'mano_derecha':forms.Select(attrs={'class': 'form-control'}),
            'historiaClinica':forms.TextInput(attrs={'class': 'form-control '}),
        }