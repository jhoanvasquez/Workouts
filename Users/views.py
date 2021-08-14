from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.migrations.recorder import MigrationRecorder
from django.core.cache import cache
from django.contrib import messages
from .forms import RegistroForm, SkillsForm, UserForm
from WorkoutsApp.models import Usuarios, Habilidades




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
        if formRegister.is_valid() :
            formRegister.save()
    #         return redirect('register2')
    #     else:
    #         print(formRegister.errors)
    return render(request, 'Users/register.html', context)
    
#Registro de habilidades
def registerSkills(request):

    formSkills = SkillsForm(request.POST or None)

    context = {
        'user_id':Usuarios.objects.latest('id').id,
        'list' : ["resistencia", "fuerza", "velocidad", "aceleracion", "agilidad", "flexibilidad", "coordinacion", "precision"]
    }
    if request.POST:
        print(request.POST)
        if formSkills.is_valid():
            formSkills.save()
            return redirect('login')
        else:
            print(formSkills.errors)
    return render(request, 'Users/register2.html', context)


def login(request):
    
    if request.POST:
        user = request.POST.get('user')
        password = request.POST.get('password')
        
        if Usuarios.objects.filter(correo=user, contra=password).exists():
            cache.set("currentUser",user,None)
        
            return redirect('perfil')
    return render(request, 'Users/login.html')

def logout(request):
    cache.clear()
    return redirect('login')


#Ver perfil de usuario
def perfil(request):
   
    return render(request, 'Users/perfil.html')


#modificar usuario
def update(request):
    usuario = cache.get("currentUser")
    updateUser =  Usuarios.objects.filter(correo=usuario)
    
    
    if request.POST:
        for data in updateUser:
            obj, created = Usuarios.objects.update_or_create(
            
            nombre = data.nombre, 
            apellidos= data.apellidos,
            edad= data.edad, 
            peso= data.peso, 
            estatura= data.estatura,
            correo= data.correo, 
            contra= data.contra, 
            ciudad= data.ciudad, 
        
            defaults={
            'nombre':updateUser.values('nombre'), 
            'apellidos':updateUser.values('apellidos'),
            'edad':request.POST.get('edad'),
            'peso':request.POST.get('peso'),
            'estatura':request.POST.get('estatura'),
            'ciudad':request.POST.get('ciudad')},)

        #redirect and try chatch
       
    context = {
        "updateUser" : updateUser
    }
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