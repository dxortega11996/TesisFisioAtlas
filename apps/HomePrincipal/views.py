from django.shortcuts import render
from django.http import HttpResponse
from apps.Profesional.models import Profesional
# Create your views here.

def index(request):
    data={}
    
    return render(request, 'Home/Home.html',data)

def paginaNosotros(request):
    data={}
    return render(request, 'Home/Nosotros.html',data)

def paginaContacto(request):
    data={}
    return render(request, 'Home/Contacto.html',data)

def paginaServicios(request):
    data={}
    return render(request, 'Home/Servicios.html',data)

def paginaHorarios(request):
    data={}
    return render(request, 'Home/Horario.html',data)
