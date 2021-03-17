from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#import django.contrib.auth.forms import User
#from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm
from .models import UserModel
from django.db.migrations.recorder import MigrationRecorder

#from WorkoutsApp.models import Prueba


# Create your views here.

def register(request): 
    #preguntar si es post
    #Instanciar el form
    #form.save()

    #print(request.POST)
    """last_migration = MigrationRecorder.Migration.objects.latest('id')
    print(last_migration.app)     
    print(last_migration.name) """

    formRegister = RegistroForm(request.POST or None)
    context = {
        'form' : formRegister
    }
    if request.POST:
        if formRegister.is_valid:
            formRegister.save()
            return redirect('register2')
    return render(request, 'Users/register.html', context)
    

def registerSkills(request):
    context = {
        'list' : ["resistencia", "fuerza", "velocidad", "aceleración", "Agilidad", "flexibilidad", "coordinación", "precisión"]
    }
    print(request.POST)
    return render(request, 'Users/register2.html', context)


def login(request):
    if request.POST:
        global user
        user = request.POST.get('user')
        password = request.POST.get('password')
        user_id = UserModel.objects.filter(email=user)
        if UserModel.objects.filter(email=user).exists() and UserModel.objects.filter(password=password).exists():
            #token = Token.objects.get_or_create(user=user_instance)
            #print(token.key)
            context = {
                 "user_active" : user
             }
             
            return render(request, 'Users/perfil.html', context)
            #return HttpResponse("<h2>¡Estas logeado!</h2>")
    #print(UserModel.objects.filter(genero="masculino"))
    return render(request, 'Users/login.html')

def perfil(request):
   
    return render(request, 'Users/perfil.html')

def update(request):
    
    return render(request, 'Users/editarPerfil.html')

def cambiarContra(request):
    context = {
                "user_active" : user
            }
    return render(request, 'Users/cambiarContra.html', context)