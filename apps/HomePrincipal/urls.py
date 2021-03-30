from django.conf.urls import url
from django.urls import path
from apps.HomePrincipal.views import index, paginaNosotros, paginaContacto,paginaServicios,paginaHorarios
app_name='indexHome'

urlpatterns=[
    path(r'',index,name="HomePrincipal"),
    path('Home/Nosotros/',paginaNosotros,name="HomeNosotros"),
    path('Home/Contacto/',paginaContacto,name="HomeContacto"),
    path('Home/Servicios/',paginaServicios,name="HomeServicios"),
    path('Home/Horarios/',paginaHorarios,name="HomeHorarios"),

    
]
