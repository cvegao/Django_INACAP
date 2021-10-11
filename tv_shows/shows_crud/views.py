from django.contrib import messages
from django.shortcuts import render, redirect

from shows_crud.models import Show


def new_show(request):
    return render(request, 'shows_crud/create_form.html')


def create_show(request):
    errors = Show.objects.validations(request.POST)

    if len(errors) == 0:
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
        context = {'show': show}
        return render(request, 'shows_crud/read_one.html', context)

    else:
        for key, msg in errors.items():
            messages.error(request, msg)
        context = {'show': request.POST}

    return render(request, 'shows_crud/create_form.html', context)


def edit_show(request, id):
    show = Show.objects.get(id=id)
    return render(request, 'shows_crud/edit_form.html', {'show': show})


def update_show(request):
    errors = Show.objects.validations(request.POST)
    show = Show.objects.get(id=request.POST['id'])

    if len(errors) == 0:
        show = Show.objects.update(
            id=request.POST['id'],
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
        return redirect('read_one', id=request.POST['id'])

    else:
        for key, msg in errors.items():
            messages.error(request, msg)
        return render(request, 'shows_crud/edit_form.html', {'show': show})


def read_all(request):
    shows = Show.objects.all()
    return render(request, 'shows_crud/read_all.html', {'shows': shows})


def read_one(request, id):
    show = Show.objects.get(id=id)
    return render(request, 'shows_crud/read_one.html', {'show': show})


def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('read_all')
