from time import strftime, gmtime

from django.shortcuts import render

# Create your views here.
from time_display import services


def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M %p", gmtime()),
    }

    return render(request, "index.html", context)


def api_index(request):
    context = {
        "time": services.get_datetime()
    }
    return render(request, "index.html", context)
