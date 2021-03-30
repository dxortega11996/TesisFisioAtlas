from django.contrib.auth.models import User
from apps.Profesional.models import Profesional
from django import forms
class Profesionalform(forms.ModelForm):
    class Meta:
        model=Profesional
        fields=[
            'cedula',
            'telefono',
            'fecha_nacimiento',
            'nacionalidad',
            'foto',
            'autoidentificacion',
            'formacion',
            'codigoMSP',
        ]
        labels={
            'cedula':'Cédula',
            'telefono':'Teléfono',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'nacionalidad':'Nacionalidad',
            'foto':'Foto',
            'autoidentificacion':'Autoidentificación',
            'formacion':'Formación  profesional',
            'codigoMSP':'Código MSP',
            }
        widgets={
            'cedula':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'fecha_nacimiento':forms.TextInput(attrs={'class': 'form-control datepicker', 'type':'date'}),
            'nacionalidad':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'foto':forms.FileInput(attrs={'class': 'form-control-file'}),
            'autoidentificacion':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'formacion':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'codigoMSP':forms.TextInput(attrs={'class':'form-control', 'required':True }),
        }

