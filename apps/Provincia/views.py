from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User



from django.contrib import messages

from apps.Provincia.models import Provincia
from apps.Canton.models import Canton
from django.http import JsonResponse

import json
from collections import Counter
# Create your views here.


def buscarCantones(request):
    results=[]
    idProvincia=request.GET.get('idProvincia')
    if request.method == 'GET':
        cantones=Canton.objects.all().filter(provincia_id= idProvincia)
        for i in cantones:
            doctor_json = {}
            doctor_json['id'] = i.id
            doctor_json['titulo']=i.nombre
            results.append(doctor_json)
        data_json=json.dumps(results) 

    else:data_json='fail'
    mimetype="application/json"
    return HttpResponse(data_json,mimetype)

    