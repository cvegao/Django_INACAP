from django.shortcuts import render

from polls.models import Client


def index(request):
    return render(request, 'polls/index.html')


def show_clients(request):
    context = {
        'list_items': Client.objects.all(),
        'attr_names': [
            'id',
            'first_name',
            'last_name',
            'email',
            'joined_datetime'
        ]
    }
    return render(request, 'polls/tables.html', context)
