from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.migrations.recorder import MigrationRecorder
from django.contrib import messages
from .forms import RegistroForm, SkillsForm
from .models import UserModel


#from WorkoutsApp.models import Prueba


# Create your views here.

#Registro de usuario
def register(request): 
    
    formRegister = RegistroForm(request.POST or None)
    context = {
        'form' : formRegister
    }
    if request.POST:
        if formRegister.is_valid() :
            formRegister.save()
            return redirect('register2')
    return render(request, 'Users/register.html', context)
    
#Registro de habilidades
def registerSkills(request):

    formSkills = SkillsForm(request.POST or None)

    context = {
        'user_id':UserModel.objects.latest('id').id,
        'list' : ["resistencia", "fuerza", "velocidad", "aceleración", "Agilidad", "flexibilidad", "coordinación", "precisión"]
    }
    if request.POST:
        print(request.POST)
        if formSkills.is_valid():
            formSkills.save()
            return redirect('login')
    return render(request, 'Users/register2.html', context)


def login(request):
    if request.POST:
        user = request.POST.get('user')
        password = request.POST.get('password')
        
        if UserModel.objects.filter(email=user).exists() and UserModel.objects.filter(password=password).exists():
            global currentUser
            currentUser = user
        
            return redirect('perfil')
    return render(request, 'Users/login.html')

def logout(request):
    currentUser = None
    return redirect('login')


#Ver perfil de usuario
def perfil(request):
   
    return render(request, 'Users/perfil.html')


#modificar usuario
def update(request):

    updateUser =  UserModel.objects.get(pk=1)
    
    if request.POST:
        
        formulario = RegistroForm(request.POST, instance=updateUser)
        if formulario.is_valid:
            formulario.save()
    
    context = {
        "updateUser" : updateUser
    }
    messages.success(request, 'Tu perfil ha sido actualizado.')
    return render(request, 'Users/editarPerfil.html', context)

def cambiarContra(request):
    if currentUser != None:
        context = {
        "user_active" : currentUser
        }
        return render(request, 'Users/cambiarContra.html', context)

#Ver progreso del usuario
def ranges(request):
    
    return render(request, 'Users/rangos.html')