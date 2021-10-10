from django.http.response import JsonResponse
from django.shortcuts import HttpResponse, redirect


def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")


def root(request):
    return redirect("/blogs")


def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse("placeholder para mostrar el blog numero: {}".format(number))


def edit(request, number):
    return HttpResponse("placeholder para editar el blog {}".format(number))


def destroy(request, number):
    return redirect("/")


def show_as_json(request):
    blogs_dict = {
        "title": "Blogs",
        "total": 100,
    }
    return JsonResponse(blogs_dict)
