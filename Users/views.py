from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.migrations.recorder import MigrationRecorder
from django.core.cache import cache
from django.contrib import messages
from .forms import RegistroForm, SkillsForm, UserForm, UserFormUpdate, RegistroFormUpdate
from WorkoutsApp.models import Usuarios, Habilidades, Rangos




#from WorkoutsApp.models import Prueba


# Create your views here.

#Registro de usuario
def register(request): 
    
    formRegister = UserForm(request.POST or None)
    formRegister2 = RegistroForm(request.POST or None)
    context = {
        'form' : formRegister,
        'form2' : formRegister2
    }
    if request.POST: 
        if formRegister.is_valid() and formRegister2.is_valid():
            formRegister.save()

            edad = request.POST.get('edad')
            peso = request.POST.get('peso')
            estatura = request.POST.get('estatura')
            ciudad = request.POST.get('ciudad')
            
            user_id = User.objects.last()
            rango_id = Rangos.objects.last()
            
            usuarios = Usuarios(edad=edad, peso=peso, estatura=estatura, fk_user=user_id, puntaje_habilidades=0, id_rango=rango_id)
            usuarios.save()

            return redirect('register2')
    
    return render(request, 'Users/register.html', context)
    
#Registro de habilidades
def registerSkills(request):

    formSkills = SkillsForm(request.POST or None)

    context = {
        'user_id': User.objects.last(),
        'list' : ["resistencia", "fuerza", "velocidad", "aceleracion", "agilidad", "flexibilidad", "coordinacion", "precision"]
    }
    if request.POST:
        resistencia = request.POST.get('resistencia')
        fuerza = request.POST.get('fuerza')
        velocidad = request.POST.get('velocidad')
        aceleracion = request.POST.get('aceleracion')
        agilidad = request.POST.get('agilidad')
        flexibilidad = request.POST.get('flexibilidad')
        coordinacion = request.POST.get('coordinacion')
        precision = request.POST.get('precision')
        print(resistencia)
        if formSkills.is_valid():

            user_id = User.objects.last()
            rango_id = Rangos.objects.last()
            
            habilidades = Habilidades(
                resistencia=resistencia, 
                fuerza=fuerza, 
                velocidad=velocidad, 
                aceleracion=aceleracion, 
                agilidad=agilidad, 
                flexibilidad=flexibilidad, 
                coordinacion=coordinacion, 
                precision=precision, 
                fk_user=user_id, 
                id_rango=rango_id
                )

            habilidades.save()
            return redirect('login')
        else:
            print(formSkills.errors)
    return render(request, 'Users/register2.html', context)


def loginView(request):
    
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(perfil)
        else:
            print('error')
    return render(request, 'Users/login.html')  

def logoutView(request):
    
    logout(request)
    return redirect('login')


#Ver perfil de usuario
@login_required()
def perfil(request):

    return render(request, 'Users/perfil.html')


#modificar usuario
@login_required()
def update(request):
    
    formRegister = UserFormUpdate(request.POST or None)
    formRegister2 = RegistroForm(request.POST or None)
    context = {
        'form' : formRegister, 
        'form2' : formRegister2
    }
    print(request.POST)
    if request.POST:
        form = UserFormUpdate(data=request.POST, instance=request.user)
    
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            edad = request.POST.get('edad')
            peso = request.POST.get('peso')
            estatura = request.POST.get('estatura')
            ciudad = request.POST.get('ciudad')

            usuarios, created = Usuarios.objects.update_or_create(
                fk_user=request.user,
                defaults={'edad': edad, 'peso': peso, 'estatura': estatura, 'ciudad':ciudad},
            
            )
            
            return redirect('perfil')
        else:
            print(form.errors) 
        
    return render(request, 'Users/editarPerfil.html', context)

def cambiarContra(request):
    '''if currentUser != None:
        context = {
        "user_active" : currentUser
        }'''
    return render(request, 'Users/cambiarContra.html')

#Ver progreso del usuario
def ranges(request):
    
    return render(request, 'Users/rangos.html')