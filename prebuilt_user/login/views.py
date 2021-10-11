from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def doStuff(request):
    testuser = authenticate(username=request.POST['username'], password=request.POST['password'])
    login(request,testuser)
    print(request.user.first_name)


def register(request):
    form = AuthenticationForm
    form2 = UserCreationForm(request.POST)
    print(form2.is_valid())
    if form2.is_valid():
      user = form2.save(commit=False) # commit = False crea un nuevo objeto de usuario que aun no esta en la BD
      user.save() # sino teniamos nada mas que hacer con el usuario.
    print(form2.errors)
    return render(request, "testUser/index.html", {"form":form(), "form2":form2})



