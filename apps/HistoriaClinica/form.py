from django.contrib.auth.models import User
from apps.HistoriaClinica.models import HistoriaClinica
from django import forms

class HistoriaClinicaform(forms.ModelForm):
    class Meta:
        model=HistoriaClinica
        fields=[
            'paciente',
            'fecha_atencion',
            'fecha_nacimiento',
            'sexo',
            'estado_civil',
            'provinciaResidencia',
            'cantonResidencia',
            'parroquia',
            'barrio',
            'dependiente',
            'nombre_representante',
            'cedula_representante',
            
            'peso',
            'temperatura',
            'talla',
            'presion_arterial',
            'imc',
            'frec_respiratoria',
            'frec_cardiaca',
           

            'actividad_fisica',
            'alimentacion',
            'consumo',

            'nombre_medicamento',
            'nombre_comercial',
            'administracion',
            'frecuencia',
            'patologias',
            'inter_quirurgica',

            'hta',
            'dm',
            'dislipidemias',
            'ecv',
            'alergias',
            'cancer',
            'otros',
            
            'motivo_consulta',

            'estado_funcional',
            'revision_aparatos',

            'inspeccion',
            'palpacion',
            'flexion',
            'extension',
            'signo_schober',

            'calificar',

            'diag_clinico',
            'diag_fisioterapeutico',

            'examen_complementario',
            'diagnostico_clinico',
            'pronostico',

            'objetivo_inicialI',
            'objetivo_intervencionI',
            'plan_tratamientoI',
            'objetivo_inicialII',
            'objetivo_intervencionII',
            'plan_tratamientoII',
            'objetivo_intervencionIII',
            'plan_tratamientoIII',
            'plan_cuidadoIII',

            'resultados',
            'anexos',

        ]
        labels={
            'paciente':'Paciente',
            'fecha_atencion':'Fecha Atencion',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'sexo':'Sexo',
            'estado_civil':'Estado Civil',
            'provinciaResidencia':'Provincia Residencia',
            'cantonResidencia':'Canton Residencia',
            'parroquia':'Parroquia',
            'barrio':'Barrio',
            'dependiente':'Dependiente',
            'nombre_representante':'Nombre Representante',
            'cedula_representante':'Cedula Representante',
            
            'peso':'Peso',
            'temperatura':'Temperatura',
            'talla':'Talla',
            'presion_arterial':'Presion Arterial',
            'imc':'IMC',
            'frec_respiratoria':'Frecuencia respiratoria',
            'frec_cardiaca':'Frecuencia Cardiaca',

            'actividad_fisica':'Actividad Fisica',
            'alimentacion':'Alimentacion',
            'consumo':'Consumo',

            'nombre_medicamento':'Nombre medicamento',
            'nombre_comercial':'Nombre comercial',
            'administracion':'Administracion',
            'frecuencia':'Frecuencia',
            'patologias':'Patologias',
            'inter_quirurgica':'Intervención quirurgica',

            'hta':'HTA',
            'dm':'DM',
            'dislipidemias':'Dislipidemias',
            'ecv':'ECV',
            'alergias':'Alergias',
            'cancer':'Cancer',
            'otros':'Otros',
            
            'motivo_consulta':'Motivo Consulta',

            'estado_funcional':'Estado Funcional',
            'revision_aparatos':'Revisión Aparatos',

            'inspeccion':'Inspección',
            'palpacion':'Palpación',
            'flexion':'Flexión',
            'extension':'Extensión',
            'signo_schober':'Signo Schober',

            'calificar':'Calificar',

            'diag_clinico':'Diagnóstico clínico',
            'diag_fisioterapeutico':'Diagnóstico fisioterapeutico',

            'examen_complementario':'Examen complementario',
            'diagnostico_clinico':'Diagnostico Clinico',
            'pronostico':'Pronóstico',

            'objetivo_inicialI':'Objetivo inicial I',
            'objetivo_intervencionI':'Objetivo intervencion I',
            'plan_tratamientoI':'Plan tratamiento I',
            'objetivo_inicialII':'Objetivo inicial II',
            'objetivo_intervencionII':'Objetivo intervencion II',
            'plan_tratamientoII':'Plan tratamiento II',
            'objetivo_intervencionIII':'Objetivo intervencion III',
            'plan_tratamientoIII':'Plan tratamiento III',
            'plan_cuidadoIII':'Plan cuidado III',

            'resultados':'Resultados',
            'anexos':'Anexos',

            }
        widgets={
            
            'paciente':forms.TextInput(attrs={'class':'form-control' }),
            'fecha_atencion':forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date' }),
            'fecha_nacimiento':forms.TextInput(attrs={'class': 'form-control datepicker', 'type': 'date' }),
            'sexo':forms.Select(attrs={'class': 'form-control'}),
            'estado_civil':forms.Select(attrs={'class': 'form-control'}),
            'provinciaResidencia':forms.Select(attrs={'class': 'form-control'}),
            'cantonResidencia':forms.Select(attrs={'class': 'form-control'}),
            'parroquia':forms.TextInput(attrs={'class':'form-control' }),
            'barrio':forms.Select(attrs={'class': 'form-control'}),
            'dependiente':forms.Select(attrs={'class': 'form-control'}),
            'nombre_representante':forms.TextInput(attrs={'class':'form-control' }),
            'cedula_representante':forms.TextInput(attrs={'class':'form-control' }),            

            'peso':forms.TextInput(attrs={'class':'form-control' }),
            'temperatura':forms.TextInput(attrs={'class':'form-control' }),
            'talla':forms.TextInput(attrs={'class':'form-control' }),
            'presion_arterial':forms.TextInput(attrs={'class':'form-control' }),
            'imc':forms.TextInput(attrs={'class':'form-control' }),
            'frec_respiratoria':forms.TextInput(attrs={'class':'form-control' }),
            'frec_cardiaca' :forms.TextInput(attrs={'class':'form-control' }),

            'actividad_fisica':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'alimentacion':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'consumo':forms.Select(attrs={'class': 'form-control'}),

            'nombre_medicamento':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial':forms.TextInput(attrs={'class':'form-control'}),            
            'administracion':forms.TextInput(attrs={'class':'form-control'}),
            'frecuencia':forms.TextInput(attrs={'class':'form-control'}),
            'patologias':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),          
            'inter_quirurgica':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),

            'hta':forms.TextInput(attrs={'class':'form-control'}),
            'dm':forms.TextInput(attrs={'class':'form-control'}),            
            'dislipidemias':forms.TextInput(attrs={'class':'form-control'}),
            'ecv':forms.TextInput(attrs={'class':'form-control'}),
            'alergias':forms.TextInput(attrs={'class':'form-control'}),            
            'cancer':forms.TextInput(attrs={'class':'form-control'}),
            'otros':forms.TextInput(attrs={'class':'form-control'}),

            'motivo_consulta':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),

            'estado_funcional':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'revision_aparatos':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),

            'inspeccion':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'palpacion':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'flexion':forms.TextInput(attrs={'class':'form-control'}),
            'extension':forms.TextInput(attrs={'class':'form-control'}),
            'signo_schober':forms.TextInput(attrs={'class':'form-control'}),            
            
            'calificar':forms.TextInput(attrs={'class':'form-control'}),
            
            'diag_clinico':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),           
            'diag_fisioterapeutico':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            
            'examen_complementario':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'diagnostico_clinico':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'pronostico':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            
            'objetivo_inicialI':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'objetivo_intervencionI':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'plan_tratamientoI':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'objetivo_inicialII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'objetivo_intervencionII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'plan_tratamientoII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            
            'objetivo_intervencionIII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'plan_tratamientoIII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),
            'plan_cuidadoIII':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),            

            'resultados':forms.Textarea(attrs={'class': 'form-control textoAmplio' }),            
            'anexos':forms.Textarea(attrs={'class': 'form-control textoAmplio'}),

        }