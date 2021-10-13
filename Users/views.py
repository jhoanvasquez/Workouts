from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.migrations.recorder import MigrationRecorder
from django.core.cache import cache
from django.contrib import messages
from .forms import RegistroForm, SkillsForm, UserForm, UserFormUpdate, RegistroFormUpdate
from WorkoutsApp.recomendador import *
from WorkoutsApp.models import Usuarios, Habilidades, Rangos

#from WorkoutsApp.models import Prueba


# Create your views here.

#Registro de usuario
@login_required()
def index(request): 
    usuario = Usuarios.objects.get(fk_user = request.user)
    skills = Habilidades.objects.get(fk_user = request.user)
    print(skills)
    puntaje = int(usuario.puntaje_habilidades) 
    context = {
        'rango' : usuario,
        'skills': skills,
        'puntaje':puntaje*20,
        'list' : ["resistencia", "fuerza", "velocidad", "aceleracion", "agilidad", "flexibilidad", "coordinacion", "precision"]
    }
    return render(request, 'Users/index.html', context)


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
            
            usuarios = Usuarios(edad=edad, peso=peso, estatura=estatura, ciudad = ciudad, fk_user=user_id, puntaje_habilidades=0, id_rango=rango_id)
            usuarios.save()

            return redirect('register2')
    
    return render(request, 'Users/register.html', context)
    
#Registro de habilidades
def registerSkills(request):

    formSkills = SkillsForm(request.POST or None)

    context = {
        'user_id': User.objects.last(),
        'list' : ["resistencia", "fuerza", "velocidad", "aceleracion", "agilidad", "flexibilidad", "coordinacion", "precision"],
        'list2' : ["Resistencia", "Fuerza", "Velocidad", "Aceleración", "Agilidad", "Flexibilidad", "Coordinación", "precisión"]
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

            
            rango = calculoRango([resistencia, fuerza, velocidad, aceleracion, agilidad, flexibilidad, coordinacion, precision])
            rango_instance = Rangos.objects.filter(id_rango = rango[0])
            usuario, created = Usuarios.objects.update_or_create(
                fk_user=user_id,
                defaults={'puntaje_habilidades': rango[1], 'id_rango': Rangos.objects.get(id_rango = rango[0])},
            )
            habilidades.save()
            return redirect('login')
        else:
            print(formSkills.errors)
    return render(request, 'Users/register2.html', context)


def loginView(request):

    if(request.user.is_authenticated):
        return render(request, 'Users/index.html')

    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            context={
                'msj': True,
                'mensaje': 'Usuario o contraseña erroneos, valide por favor'
            }
            return render(request, 'Users/login.html', context)

    return render(request, 'Users/login.html')  

def logoutView(request):
    
    logout(request)
    return redirect('login')


#Ver perfil de usuario
@login_required()
def perfil(request):
    return render(request, 'Users/perfil.html')


#Ver vista 404
def error404(request, exception):
    return render(request, 'Users/404.html')

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


def calculoRango(skills):

    numero_rangos = len(Rangos.objects.all())
    rango_id = 0
    acumulador = 0
    for skill in skills:
        acumulador += int(skill)
    
    acumulador = (acumulador / 8)

    if(acumulador < 5/numero_rangos):
        rango_id = 1
    if(acumulador > (5/numero_rangos) and acumulador < (5/numero_rangos)*2):
        rango_id = 2
    if(acumulador > (5/numero_rangos)*2):
        rango_id = 3
    
    return (rango_id, acumulador)