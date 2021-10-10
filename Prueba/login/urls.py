from django.urls import path, include
from . import views

#Aqui se registra las rutas de la aplicacion 
urlpatterns = [
    path('', views.login),#ruta por defecto al iniciar la aplicacion, redireccionando al metodo login
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
]