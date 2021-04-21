from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User

from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView

from django.contrib import messages
from apps.Paciente.models import Paciente
from apps.Profesional.models import Profesional
from django.contrib.auth.hashers import make_password

from apps.Paciente.form import Pacienteform, Userform
from apps.HistoriaClinica.form import HistoriaClinicaform
from apps.Provincia.models import Provincia
from apps.HistoriaClinica.models import HistoriaClinica
from apps.Rutina.models import Rutina
from apps.Juego.models import Juego
from apps.RutinaJuego.models import RutinaJuego
from apps.Control.models import Control
from apps.Rutina.form import Rutinaform


from apps.Progreso.models import Progreso
from apps.Intento.models import Intento

from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q

# Create your views here.


class listarPaciente(ListView):
    model = Paciente
    template_name='Paciente/ListarPaciente.html'
    def get_context_data(self, **kwargs):
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        profesionalId=Profesional.objects.filter(user_id=self.request.user.id).first()
        context = super().get_context_data(**kwargs)
        context['pacientes']=Paciente.objects.all().filter(profesional_id=profesionalId.id)
        context['Profesional']=perfil
        return context

class RegistrarPaciente(CreateView):
        model = Paciente
        template_name = "Paciente/RegistrarPaciente.html"
        form_class = Pacienteform
        second_form_class = Userform
        success_url = reverse_lazy('Paciente:listarPaciente')
        def get_context_data(self, **kwargs):
            
            pk = self.request.user.id
            perfil = Profesional.objects.get(user_id=pk)
            context= super(RegistrarPaciente,self).get_context_data(**kwargs)
            if 'form' not in context:
                context['form']= self.form_class(self.request.GET)
            if 'form2' not in context:
                context['form2']= self.second_form_class(self.request.GET)
            context['Profesional']=perfil
            return context
        def post(self, request, *args, **kwargs):
            self.object= self.get_object
            form= self.form_class(request.POST)#empleado
            form2 = self.second_form_class(request.POST)#usuario
            profesionalId=Profesional.objects.filter(user_id=self.request.user.id).first()
            if form.is_valid() and form2.is_valid():
                paciente = form.save(commit=False)
                paciente.user = form2.save()
                paciente.profesional_id= profesionalId.id
                paciente.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(request,('Por favor registrese nuevamente..!!'))
                return self.render_to_response(self.get_context_data(form=form, form2=form2))
    

class ActualizarPaciente(UpdateView):
    model=Paciente
    second_model=User
    template_name = "Paciente/ActualizarPaciente.html"
    form_class =Pacienteform 
    second_form_class = Userform
    success_url = reverse_lazy('Paciente:listarPaciente')
    def get_context_data(self, **kwargs):
        pku = self.request.user.id
        perfil = Profesional.objects.get(user_id=pku)
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs.get('pk',0)
        empleadoid=self.model.objects.get(id=pk)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        if 'form' not in context:
            context['form']= self.form_class()
        if 'form2' not in context:
            context['form2']= self.second_form_class(instance=user)
        context['id']=pk
        context['Profesional']=perfil
        return context
    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        id_empleado=self.kwargs.get('pk',0)
        empleadoid= self.model.objects.get(id=id_empleado)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        form = self.form_class(request.POST, instance=empleadoid)
        form2= self.second_form_class(request.POST, instance=user) 
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request,('Por favor intente nuevamente'))
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class EliminarPaciente(DeleteView):
    model=Paciente
    template_name ='Paciente/EliminarPaciente.html'
    success_url = reverse_lazy('Paciente:listarPaciente')

class VisualHistoriaClinica(UpdateView):
    model=Paciente
    second_model=User
    third_model=HistoriaClinica
    template_name = "HistoriaClinica/ActualizarHistoriaClinica.html"
    form_class =Pacienteform 
    second_form_class = Userform
    third_form_class=HistoriaClinicaform
    success_url = reverse_lazy('Paciente:listarPaciente')
    def get_context_data(self, **kwargs): 
        pku = self.request.user.id
        perfil = Profesional.objects.get(user_id=pku)
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs.get('pk',0)
        empleadoid=self.model.objects.get(id=pk)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        historiaClinica=self.third_model.objects.get(paciente_id=empleadoid.id)
        if 'form' not in context:
            context['form']= self.form_class()
        if 'form2' not in context:
            context['form2']= self.second_form_class(instance=user)
        if 'form3' not in context:
                context['form3']= self.third_form_class(instance=historiaClinica)
        context['id']=empleadoid.id
        context['provincias'] = Provincia.objects.all().order_by('nombre')
        context['profesional']=Profesional.objects.get(user=self.request.user.id)
        context['Profesional']=perfil
        
        return context
    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        id_empleado=self.kwargs.get('pk',0)
        empleadoid= self.model.objects.get(id=id_empleado)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        historiaClinica=self.third_model.objects.get(paciente_id=empleadoid.id)
        form = self.form_class(request.POST, instance=empleadoid)
        form2= self.second_form_class(request.POST, request.FILES,instance=user) 
        form3 = self.third_form_class(request.POST, request.FILES,instance=historiaClinica)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request,('Por favor intente nuevamente'))
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class listarSeguimientoPaciente(ListView):
    model = Paciente
    template_name='Seguimiento/ListarSeguimiento.html'
    def get_context_data(self, **kwargs):
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        profesionalId=Profesional.objects.filter(user_id=self.request.user.id).first()
        context = super().get_context_data(**kwargs)
        context['pacientes']=Paciente.objects.all().filter(historiaClinica = 'SI',profesional_id=profesionalId.id) 
        context['Profesional']=perfil
        
        return context

def activarHC(request):
    idPaciente= request.POST.get('idPaciente')
   
    if request.method == 'POST':
        Paciente.objects.filter(pk=idPaciente).update(
            historiaClinica='SI'
        )

    hc=HistoriaClinica.objects.filter(paciente_id=idPaciente)
    
    if hc :
        print('existe')
    else:
        historiaC= HistoriaClinica.objects.create(paciente_id=idPaciente)
        historiaC.save()
    
    return HttpResponseRedirect('/paciente/listarPaciente/')


def eliminarPacineteV2(request):
    idPaciente= request.POST.get('idPaciente')
    if request.method == 'POST':
        pacienteInfo=Paciente.objects.get(pk=idPaciente)
        if pacienteInfo.user_id:
            User.objects.filter(pk=pacienteInfo.user_id).delete()
            pacienteInfo.delete()
    return HttpResponseRedirect('/paciente/listarPaciente/')


class RegistrarRutina(CreateView):
        model = Rutina
        template_name = "Seguimiento/CrearRutina.html"
        form_class = Rutinaform
        success_url = reverse_lazy('Paciente:listarSeguimiento')
        def get_context_data(self, **kwargs):
            
            context= super(RegistrarRutina,self).get_context_data(**kwargs)
            pku = self.request.user.id
            perfil = Profesional.objects.get(user_id=pku)
            idPacinete = self.kwargs.get('pk',0)
            idPHC=Paciente.objects.filter(user_id=idPacinete).first()
            
            if 'form' not in context:
                context['form']= self.form_class(self.request.GET)
            context['paciente1']=Paciente.objects.filter(user_id=idPacinete).first()
            context['historiaC']=HistoriaClinica.objects.filter(paciente_id=idPHC.id).first()
            context['Juegos']=Juego.objects.all()
            context['Profesional']=perfil
            
            return context
        def post(self, request, *args, **kwargs):
            self.object= self.get_object
            form= self.form_class(request.POST)#empleado
            
            if form.is_valid() :
                vRutina = form.save()
                vRutina.save()
                idRutina=vRutina.id
               
                idUsuario = self.kwargs.get('pk',0)
                idPaciente=Paciente.objects.filter(user_id=idUsuario).first()
                idPac = idPaciente.id
                Paciente.objects.filter(pk=idPac).update(
                    seguimiento='SI'
                )
                numSesion1=1
                juego1= request.POST['juegonNum1']
               
                if juego1=='SI':
                    numsesionesJuego1=request.POST['NumSesionesJuego1']  
                    for i in range(int(numsesionesJuego1)):
                        newControl=Control.objects.create(rutina_id=idRutina,numeroSesion=numSesion1,juego_id=1)
                        numSesion1+=1
                        newControl.save()
                
                
                numSesion2=1
                juego2= request.POST['juegonNum2'] 
                if juego2=='SI':
                  numsesionesJuego2=request.POST['NumSesionesJuego2']  
                  for i in range(int(numsesionesJuego2)):
                    newControl=Control.objects.create(rutina_id=idRutina,numeroSesion=numSesion1,juego_id=2)
                    numSesion1+=1
                    newControl.save()

                numSesion3=1
                juego3= request.POST['juegonNum3']
                
                if juego3=='SI':
                  numsesionesJuego3=request.POST['NumSesionesJuego3']
                  for i in range(int(numsesionesJuego3)):
                    newControl=Control.objects.create(rutina_id=idRutina,numeroSesion=numSesion1,juego_id=3)
                    numSesion1+=1
                    newControl.save()

                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(request,('Por favor intente nuevamente'))
                return self.render_to_response(self.get_context_data(form=form))


class listarControlPaciente(ListView):
    model = Control
    template_name='Control/ListarControl.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        idPaciente = self.kwargs.get('pk',0)
        
        idPHC=Paciente.objects.filter(pk=idPaciente).first()
        idHistoriaC=HistoriaClinica.objects.filter(paciente_id=idPaciente).first()
        idRutina=Rutina.objects.filter(historiaClinica_id=idHistoriaC.id).first()
        controles=Control.objects.all().filter(rutina_id = idRutina.id) 
        idControles = [val.id for val in controles]
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        context['Profesional']=perfil
        context['juegos']=RutinaJuego.objects.all().filter(rutina_id=idRutina.id)
        context['Inetentos']=serializers.serialize('json', Intento.objects.all().filter(control_id__in=idControles))
        context['Progresos']=serializers.serialize('json', Progreso.objects.all().filter(control_id__in=idControles))
        context['Juegos']=serializers.serialize('json', Juego.objects.all())
        context['rutina']=idRutina
        context['controles']=Control.objects.all().filter(rutina_id = idRutina.id) 
        context['controlesJuego1']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=1) 
        context['controlesJuego2']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=2) 
        context['controlesJuego3']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=3) 
        context['ControlesNoFinalizados']=Control.objects.filter(rutina_id = idRutina.id).exclude(estado = 'FINALIZADO').count()
        
        return context

def actualizarSesion(request):
    idSesion= request.POST.get('idSesion')
    vfechaVisita= request.POST.get('fechaVisita')
    vvaloracion= request.POST.get('valoracion')
    vdolor= request.POST.get('dolor')
    
    if request.method == 'POST':
        Control.objects.filter(pk=idSesion).update(
            fecha_visita=vfechaVisita,
            valoracion=vvaloracion,
            dolor=vdolor,
            estado='FINALIZADO'
        )
    return HttpResponseRedirect('/paciente/listarPaciente/')

def finalizarRutina(request):
    idRutina= request.POST.get('idRutina')
    
    if request.method == 'POST':
        Control.objects.filter(rutina_id=idRutina).update(
            estado='FINALIZADO'
        )
    
        Rutina.objects.filter(pk=idRutina).update(
            estado='FINALIZADO'
        )
    data={}
    return render(request, 'Seguimiento/ListarSeguimiento.html',data)


class listarReportes(ListView):
    model = Paciente
    template_name='Reportes/ListarReporte.html'
    def get_context_data(self, **kwargs):
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        profesionalId=Profesional.objects.filter(user_id=self.request.user.id).first()
        context = super().get_context_data(**kwargs)
        pacientesAsig=Paciente.objects.all().filter(historiaClinica = 'SI',profesional_id=profesionalId.id) 
        idPacientes=[]
        for i in pacientesAsig:
            idPacientes.append(i.pk)
        historiascli=HistoriaClinica.objects.filter(paciente_id__in = idPacientes)

        idhistoriasClinicas=[]
        for j in historiascli:
            idhistoriasClinicas.append(j.pk)

        rutinas=Rutina.objects.filter(historiaClinica_id__in=idhistoriasClinicas,estado="FINALIZADO")
        

        context['pacientes']=Paciente.objects.all().filter(historiaClinica = 'SI',profesional_id=profesionalId.id) 
        context['Profesional']=perfil
        context['rutina']=rutinas
        
        return context

class visualizarReporte(ListView):
    model = Control
    template_name='Reportes/VisualizarReporte.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        
        idPaciente = self.kwargs.get('pk',0)
        
        idPHC=Paciente.objects.filter(pk=idPaciente).first()
        idHistoriaC=HistoriaClinica.objects.filter(paciente_id=idPaciente).first()
        idRutina=Rutina.objects.filter(historiaClinica_id=idHistoriaC.id).first()
        controles=Control.objects.all().filter(rutina_id = idRutina.id) 
        idControles = [val.id for val in controles]
       

        context['juegos']=RutinaJuego.objects.all().filter(rutina_id=idRutina.id)
        context['Inetentos']=serializers.serialize('json', Intento.objects.all().filter(control_id__in=idControles))
        context['Progresos']=serializers.serialize('json', Progreso.objects.all().filter(control_id__in=idControles))
        context['Juegos']=serializers.serialize('json', Juego.objects.all())
        context['rutina']=idRutina
        context['Controles']=serializers.serialize('json', Control.objects.all().filter(rutina_id = idRutina.id))  
        context['controlesJuego1']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=1) 
        context['controlesJuego2']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=2) 
        context['controlesJuego3']=Control.objects.all().filter(rutina_id = idRutina.id,juego_id=3) 
        context['ControlesNoFinalizados']=Control.objects.filter(rutina_id = idRutina.id).exclude(estado = 'FINALIZADO').count()
        context['Profesional']=perfil
        context['Paciente']=idPHC
        return context


class visualizarGraficas(ListView):
    model = Control
    template_name='Reportes/VisualizarGraficas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        
        idPaciente = self.kwargs.get('pk',0)
        
        idPHC=Paciente.objects.filter(pk=idPaciente).first()
        idHistoriaC=HistoriaClinica.objects.filter(paciente_id=idPaciente).first()
        idRutina=Rutina.objects.filter(historiaClinica_id=idHistoriaC.id).first()
        controles=Control.objects.all().filter(rutina_id = idRutina.id) 
        idControles = [val.id for val in controles]
       

        context['juegos']=RutinaJuego.objects.all().filter(rutina_id=idRutina.id)
        context['Inetentos']=serializers.serialize('json', Intento.objects.all().filter(control_id__in=idControles))
        context['Progresos']=serializers.serialize('json', Progreso.objects.all().filter(control_id__in=idControles))
        context['Juegos']=serializers.serialize('json', Juego.objects.all())
        


        context['rutina']=idRutina
        context['Controles']=serializers.serialize('json', Control.objects.all().filter(rutina_id = idRutina.id))  
        
        context['Profesional']=perfil
        context['Paciente']=idPHC
        return context