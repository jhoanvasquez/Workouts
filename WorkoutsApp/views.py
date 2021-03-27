from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DashboardForm
from .models import Usuarios
from .models import Planes
from .models import Areas
#from models import *  


def index(request):
    return HttpResponse("<h2>Workouts</h2>")


# Create your views here.


def register(request):
    return render(request, 'WorkoutsApp/register.html')

    
def dashboard(request):
    

    formulario=DashboardForm()
    usuarios = Usuarios.objects.all()
    areas = Areas.objects.all()
    planentreno = Planes.objects.all()
    context = {
       "nombre": request.user,
        "apellido": "Abreu",
        'form': formulario,
        "usuarios": usuarios,
        "areas": areas,
        "planentreno": planentreno
    }

    return render(request, 'dashboard.html', context )

def register(request): 
    #preguntar si es post
    #Instanciar el form
    #form.save()

    #print(request.POST)
    last_migration = MigrationRecorder.Migration.objects.latest('id')
    print(last_migration.app)     
    print(last_migration.name) 

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
    context = {
        'list' : ["resistencia", "fuerza", "velocidad", "aceleración", "Agilidad", "flexibilidad", "coordinación", "precisión"]
    }
    print(request.POST)
    return render(request, 'WorkoutsApp/register2.html', context)


def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    if UserModel.objects.filter(email=user).exists() and UserModel.objects.filter(password=password).exists():
        return HttpResponse("<h2>¡Estas logeado!</h2>")
    #print(UserModel.objects.filter(genero="masculino"))
    return render(request, 'WorkoutsApp/login.html')

