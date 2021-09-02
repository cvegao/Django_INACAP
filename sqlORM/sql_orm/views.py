import MySQLdb
from django.contrib import messages
from django.shortcuts import render, redirect

from sql_orm.forms import WizardForm
from sql_orm.models import Wizard


def index(request):
    wizard_list = Wizard.objects.all()

    return render(request, 'sql_orm/index.html', {'wizard_list': wizard_list})


def create_wizard(request):
    wizard_form = WizardForm()

    if request.method == 'POST':
        errors = Wizard.objects.validations(request.POST)

        if len(errors) == 0:
            wizard = Wizard(request.POST)
            wizard.save()
            messages.success(request, "Wizard created successfully")
            return redirect('hp_index')

        for e in errors:
            messages.error(request, e)
        return redirect('create_wizard')

    context = {
        'wizard_form': wizard_form,
        'action': 'create_wizard',
    }

    return render(request, 'sql_orm/wizard_form.html', context)


def edit_wizard_form(request):
    wizard = Wizard.objects.get(id=request.POST["id"])
    wizard_form = WizardForm(initial=wizard)

    context = {
        'wizard_form': wizard_form,
        'action': 'edit_wizard',
    }

    print(wizard_form)
    return render(request, 'sql_orm/wizard_form.html', context)


def edit_wizard(request):
    wizard = Wizard.objects.get(id=request.POST["id"])
    wizard_form = WizardForm(request.POST, initial=wizard)

    errors = Wizard.objects.validations(request.POST)
    if len(errors) == 0:
        WizardForm(request.POST).save()
        messages.success(request, "Wizard updated successfully")
        return redirect('hp_index')

    for e in errors:
        messages.error(request, e)

    context = {
        'wizard_form': wizard_form,
    }

    return render(request, 'sql_orm/wizard_form.html', context)


def delete_wizard(request):
    wizard = Wizard.objects.get(id=request.POST["id"])

    if request.method == 'POST':
        try:
            wizard.delete()
            messages.success(request, "Wizard deleted successfully")
            return redirect('hp_index')
        except MySQLdb.MySQLError:
            messages.error(request, "There was an error deleting the wizard")
            return redirect('hp_index')

    return redirect('error')


def error(request):
    return render(request, 'sql_orm/error.html')
