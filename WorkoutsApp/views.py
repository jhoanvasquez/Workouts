from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#import django.contrib.auth.forms import User
#from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm
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
    return render(request, 'WorkoutsApp/register.html', context)

def registerSkills(request):
    return render(request, 'WorkoutsApp/register2.html')

def login(request):
    return render(request, 'WorkoutsApp/login.html')