from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import loader
from datetime import datetime,date
from apps.Profesional.models import Profesional
# Create your views here.
@login_required(login_url="/accounts/login")
def inicio(request):
    usuario = request.user.pk
    perfil = Profesional.objects.get(user_id=request.user.id)
   
    data={}
    return render(request, 'Home/index.html',{'Profesional':perfil})
from django.contrib.auth import login
def new(request):
    if 'UserAll' in request.POST:
        usN = request.POST['UserAll']
        usuarioNuevo = User.objects.get(id = usN)
        usuarioNuevo.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, usuarioNuevo)
    return HttpResponseRedirect('/accounts/profile/')