from django.db import models
from apps.Provincia.models import Provincia
from apps.Canton.models import Canton
from apps.Paciente.models import Paciente
from apps.SignosVitales.models import SignosVitales
from apps.Paciente.models import Paciente

# Create your models here.
class HistoriaClinica(models.Model):
    paciente= models.OneToOneField(Paciente, on_delete=models.CASCADE, blank=True, null=True)

    CHOICES =(
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
    )
    Estado=( 
        ('Soltero(a)','Soltero(a)'),
        ('Casado(a)','Casado(a)'),
        ('Divorciado(a)','Divorciado(a)')
    )
    vDependiente=( 
        ('SI','SI'),
        ('NO','NO')
    )
    vConsumo=( 
        ('Alcohol','Alcohol'),
        ('Tabaco','Tabaco'),
        ('Drogas','Drogas'),
        ('Otros','Otros')
    )
    fecha_atencion= models.DateField(blank=True, null=True)
    fecha_nacimiento= models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=100, choices=CHOICES,blank=True, null=True)
    estado_civil=models.CharField(max_length=100,choices=Estado,blank=True, null=True)
    provinciaResidencia = models.ForeignKey(Provincia, on_delete=models.CASCADE, blank=True, null=True)
    cantonResidencia = models.ForeignKey(Canton, on_delete=models.CASCADE, blank=True, null=True)
    parroquia = models.CharField(max_length=100,null=True,blank=True)
    barrio = models.CharField(max_length=100,null=True,blank=True)
    dependiente=models.CharField(max_length=100,choices=vDependiente,blank=True, null=True)
    nombre_representante = models.CharField(max_length=100,null=True,blank=True)
    cedula_representante = models.CharField(max_length=20,null=True,blank=True)

    peso = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    temperatura = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    talla = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    presion_arterial = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    imc = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    frec_respiratoria = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    frec_cardiaca = models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
        
    actividad_fisica = models.CharField(max_length=300,null=True,blank=True)
    alimentacion = models.CharField(max_length=300,null=True,blank=True)
    consumo = models.CharField(max_length=100,choices=vConsumo,blank=True, null=True)
   
    
    nombre_medicamento= models.CharField(max_length=300,null=True,blank=True)
    nombre_comercial= models.CharField(max_length=300,null=True,blank=True)
    administracion= models.CharField(max_length=300,null=True,blank=True)
    frecuencia= models.CharField(max_length=300,null=True,blank=True)
    patologias= models.CharField(max_length=300,null=True,blank=True)
    inter_quirurgica= models.CharField(max_length=300,null=True,blank=True)
    
    hta= models.CharField(max_length=300,null=True,blank=True)
    dm= models.CharField(max_length=300,null=True,blank=True)
    dislipidemias= models.CharField(max_length=300,null=True,blank=True)
    ecv= models.CharField(max_length=300,null=True,blank=True)
    alergias= models.CharField(max_length=300,null=True,blank=True)
    cancer= models.CharField(max_length=300,null=True,blank=True)
    otros= models.CharField(max_length=300,null=True,blank=True)
    
    motivo_consulta= models.CharField(max_length=400,null=True,blank=True)
    estado_funcional= models.CharField(max_length=300,null=True,blank=True)
    revision_aparatos= models.CharField(max_length=300,null=True,blank=True)
    
    inspeccion= models.CharField(max_length=300,null=True,blank=True)
    palpacion= models.CharField(max_length=300,null=True,blank=True)
    flexion= models.DecimalField(max_digits = 5, decimal_places = 2, blank=True, null=True)
    extension= models.DecimalField(max_digits = 5, decimal_places = 2, null=True,blank=True)
    signo_schober= models.CharField(max_length=300,null=True,blank=True)
    
    calificar = models.IntegerField(null=True,blank=True)

    diag_clinico = models.CharField(max_length=400,null=True,blank=True)
    diag_fisioterapeutico = models.CharField(max_length=400,null=True,blank=True)

    examen_complementario = models.CharField(max_length=300,null=True,blank=True)
    diagnostico_clinico = models.CharField(max_length=300,null=True,blank=True)
    pronostico = models.CharField(max_length=400,null=True,blank=True)

    objetivo_inicialI = models.CharField(max_length=300,null=True,blank=True)
    objetivo_intervencionI = models.CharField(max_length=300,null=True,blank=True)
    plan_tratamientoI = models.CharField(max_length=300,null=True,blank=True)
    objetivo_inicialII = models.CharField(max_length=300,null=True,blank=True)
    objetivo_intervencionII = models.CharField(max_length=300,null=True,blank=True)
    plan_tratamientoII = models.CharField(max_length=300,null=True,blank=True)
    objetivo_intervencionIII = models.CharField(max_length=300,null=True,blank=True)
    plan_tratamientoIII = models.CharField(max_length=300,null=True,blank=True)
    plan_cuidadoIII = models.CharField(max_length=300,null=True,blank=True)

    resultados = models.CharField(max_length=400,null=True,blank=True)
    anexos = models.CharField(max_length=400,null=True,blank=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, blank=True, null=True)


    
