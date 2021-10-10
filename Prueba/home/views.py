import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User, Apointment


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['user_id'])
    reg_user.appointments.all()
    context = {
        "active_user": reg_user,
    }

    return render(request, 'home.html', context)


def index(request):
    return render(request, 'index.html')


def add(request):
    if request.method == 'POST':
        Apointment.objects.create(
            task=request.POST['task'],
            date=request.POST['date'],
            status=request.POST['status'],
            user=request.session['user_id']
        )
        return redirect('index')
    return render(request, 'add.html')
