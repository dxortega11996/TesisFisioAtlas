from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User

from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView

from django.contrib import messages
from apps.Profesional.models import Profesional
 

from apps.Profesional.form import Profesionalform
from apps.Paciente.form import Userform

from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash

from django.core.files.storage import FileSystemStorage


# Create your views here.


class RegistrarProfesional(CreateView):
        model = Profesional
        template_name = "Profesional/RegistrarProfesional.html"
        form_class = Profesionalform
        second_form_class = Userform
        success_url = reverse_lazy('Profesional:listarProfesional')
        def get_context_data(self, **kwargs):
            context= super(RegistrarProfesional,self).get_context_data(**kwargs)
            
            
            if 'form' not in context:
                context['form']= self.form_class(self.request.GET)
            if 'form2' not in context:
                context['form2']= self.second_form_class(self.request.GET)
            return context
        def post(self, request, *args, **kwargs):
            self.object= self.get_object
            form= self.form_class(request.POST)#empleado
            form2 = self.second_form_class(request.POST)#usuario

            foto=self.request.FILES['foto']
            contrasenia=request.POST['password']
            lacontrasenia=make_password(contrasenia)
            
            foto=self.request.FILES['foto']
            contrasenia=request.POST['password']
            lacontrasenia=make_password(contrasenia)
            
            if form.is_valid() and form2.is_valid():
                investigador = form.save(commit=False)
                investigador.user = form2.save()
                investigador.user.password=make_password(contrasenia)
                investigador.save()
                fs=FileSystemStorage()
                urlFoto=fs.save(foto.name,foto)
                url=fs.url(urlFoto)
                investigador.foto = url
                investigador.save()
                idUser=investigador.user.id
                

                User.objects.filter(pk=idUser).update(
                    password=lacontrasenia
                )

                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(request,('Por favor registrese nuevamente'))
                return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ActualizarProfesional(UpdateView):
    model=Profesional
    second_model=User
    template_name = "Profesional/ActualizarProfesional.html"
    form_class =Profesionalform 
    second_form_class = Userform
    success_url = reverse_lazy('Profesional:listarProfesional')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs.get('pk',0)
        empleadoid=self.model.objects.get(id=pk)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        if 'form' not in context:
            context['form']= self.form_class()
        if 'form2' not in context:
            context['form2']= self.second_form_class(instance=user)
        context['id']=pk
        return context
    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        id_empleado=self.kwargs.get('pk',0)
        empleadoid= self.model.objects.get(id=id_empleado)
        user=self.second_model.objects.get(id=empleadoid.user_id)
        idUser=user.id
        form = self.form_class(request.POST, instance=empleadoid)
        form2= self.second_form_class(request.POST, instance=user) 
        
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()

            contrasenia=request.POST['password']
            lacontrasenia=make_password(contrasenia)
            User.objects.filter(pk=idUser).update(
                    password=lacontrasenia
                )
            validar = request.POST['validarFoto']
            if validar == 'SI':
                foto=self.request.FILES['foto']
                if foto.name:
                    fs=FileSystemStorage()
                    urlFoto=fs.save(foto.name,foto)
                    url=fs.url(urlFoto)
                
                    Profesional.objects.filter(pk=empleadoid.id).update(
                        foto=url
                    )

            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request,('Por favor intente nuevamente'))
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class listarProfesional(ListView):
    model = Profesional
    template_name='Profesional/ListarProfesional.html'
    def get_context_data(self, **kwargs):
        pk = self.request.user.id
        perfil = Profesional.objects.get(user_id=pk)
        context = super().get_context_data(**kwargs)
        context['profesional']=Profesional.objects.exclude(user_id=pk)
        context['Profesional']=perfil
        return context

def actualizarEstado(request):
    idUser = request.POST.get('idUsuario')
    estado = request.POST.get('estado')
    if request.method == 'POST':
     User.objects.filter(pk=idUser).update(
     is_active=estado,
     
     )
    return HttpResponseRedirect('/profesional/listarProfesional/')
