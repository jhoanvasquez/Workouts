from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DashboardForm
from .models import Usuarios
from .models import Planes
from .models import Areas
from .models import Ejercicios
from .models import Rangos
from .models import Sesiones
from .models import Sesion_Ejercicio
from .models import Habilidades

from datetime import datetime


def index(request):
    return HttpResponse("<h2>Workouts</h2>")


# Create your views here.


def register(request):
    return render(request, 'WorkoutsApp/register.html')

def sesion(request):


    
    formulario=DashboardForm()
    


    return render(request, 'sesion.html')

def sugerencias(request):
    userconect = request.POST.get('user')

#    authenticate(request, username=username, password=password)

    print(userconect)
    iduser=1
       
    usuarios = Usuarios.objects.all()
    planentreno = Planes.objects.get(id_plan=iduser)
    idhabi = planentreno.id_rango_id
    
    idarea = planentreno.id_area_id
    area = Areas.objects.get(id_area=idarea)
    nombre_area = getattr(area, "descripcion")

    #ejercicios filtrados por habilidad puede ser por varias mas adelante
    #ejercicios = Ejercicios.objects.filter(id_habilidad=idhabi)
    ejercicios = Ejercicios.objects.all()

    context = {
       "nombre": request.user,
        "apellido": "Abreu",
        "usuarios": usuarios,
        "iduser": iduser,
        "area": nombre_area,
        "ejercicios": ejercicios,

        "userconect":userconect
    }

    return render(request, 'sugerencias.html', context)



def planes(request):

    #se obtiene toda la info de las tablas de la BD
    
    usuarios = Usuarios.objects.all()

    #usuario= Usuarios.objects.get(id_usuario=iduser)
    iduser=2
    
    
    #planentreno = Planes.objects.get(id_plan=iduser)
    planesentreno = Planes.objects.filter(id_usuario=iduser)

    #idhabi = planentreno.id_rango_id
    
    #idareas = planesentreno.objects

    #nombre_area = getattr(area, "descripcion")

    #ejercicios filtrados por habilidad, debe ser por sesion o como se escoja
    #ejercicios = Ejercicios.objects.filter(id_rango=idhabi) 



    context = {
       "nombre": request.user,
        "apellido": "Abreu",
        "usuarios": usuarios,
        "iduser": iduser,
        #"ejercicios": ejercicios,
        "planes": planesentreno
    }

    return render(request, 'planes.html', context )


    
def dashboard(request):

    iduser=1
    
    hoy = datetime.today().isoweekday()
    #diasrestantes=7-hoy
    diasrestantes=4
    totalentrenos=5
    
    #se obtiene toda la info de las tablas de la BD
    usuarios = Usuarios.objects.all()

    planentreno = Planes.objects.get(id_plan=iduser)
    idhabi = planentreno.id_rango_id
    
    idarea = planentreno.id_area_id
    area = Areas.objects.get(id_area=idarea)
    nombre_area = getattr(area, "descripcion")

    #ejercicios filtrados por habilidad, debe ser por sesion o como se escoja
    ejercicios = Ejercicios.objects.filter(id_rango=idhabi) 

    #ejercicios o sesiones
    #si ya hizo todos los entrenos del plan no muestra nada
    if planentreno.dias_entrenados >= totalentrenos:
        ejercicios=ejercicios[:0]
    #si aun no ha hecho todos mandar los dias faltantes de sesiones
    if planentreno.dias_entrenados < totalentrenos:
        ejercicios=ejercicios[:diasrestantes]
    


    context = {
       "nombre": request.user,
        "apellido": "Abreu",
        "usuarios": usuarios,
        "iduser": iduser,
        "area": nombre_area,
        "ejercicios": ejercicios,
        "diasrestantes":diasrestantes
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

    cod=1
    request.codigo = cod

    print (request.codigo)
    

    if UserModel.objects.filter(email=user,password=password).exists() :
        user= UserModel.objects.get(email=user,password=password)
        login(request,user)
        return HttpResponse("<h2>¡Estas logeado!</h2>")
    #print(UserModel.objects.filter(genero="masculino"))
    return render(request, 'WorkoutsApp/login.html')

