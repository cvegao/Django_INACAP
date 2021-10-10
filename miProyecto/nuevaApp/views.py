from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo!")


def mostrar_todas(request):
    pass


def mostrar_por_id(request, id):
    pass


def mostrar_variedades_por_origen(request, origen):
    pass