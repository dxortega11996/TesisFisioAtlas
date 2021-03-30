from django.contrib.auth.models import User
from apps.Paciente.models import Paciente
from django import forms

class Pacienteform(forms.ModelForm):
    class Meta:
        model=Paciente
        fields=[
            'cedula',
            'telefono',
            'fechaCita',
            'historiaClinica',
            'patologia'
        ]
        labels={
            'cedula':'Cédula',
            'telefono':'Teléfono',
            'fechaCita':'Fecha Cita',
            'historiaClinica':'historiaClinica',
            'patologia':'Patología Aparente'
            }
        widgets={
            'cedula':forms.TextInput(attrs={'class':'form-control', 'required':True }),
            'telefono':forms.TextInput(attrs={'class':'form-control ', 'required':True }),
            'fechaCita':forms.TextInput(attrs={'class': 'form-control datepicker', 'type':'date'}),
            'historiaClinica':forms.TextInput(attrs={'class': 'form-control '}),
            'patologia':forms.TextInput(attrs={'class': 'form-control '}),
            
        }

class Userform (forms.ModelForm):
    class Meta:
        model = User
        fields=[
            
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            
            
        ]
        labels={
            
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'email':'Email',
            'username':'User name',
            'password':'Contraseña'
        } 
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control SoloLetras','onkeyup':'javascript:this.value=this.value.toUpperCase();','required':True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control SoloLetras','onkeyup':'javascript:this.value=this.value.toUpperCase();','required':True}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'required':True }),
            'username':forms.EmailInput(attrs={'class':'form-control', 'required':True }),
            'password': forms.PasswordInput(attrs={'class': 'form-control','required':True })
        }