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


def sesion2(request):

    #print(request)

    if request.POST:

        print(request.POST['codigoplan'])

    formulario=DashboardForm()

    return render(request, 'sesion2.html')


def sugerencias(request):
    userconect = request.POST.get('user')

    #authenticate(request, username=username, password=password)

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

    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    codusuario = usuario.id_usuario


    planesentreno = Planes.objects.filter(id_usuario=codusuario)

#! falta filtrar planes que tengan numeros de sesiones acabadas para no mostrar

    context = {
        "nombre": request.user,
        "apellido": "Abreu",
        #"usuarios": usuarios,
        "iduser": codusuario,
        "planes": planesentreno
    }

    return render(request, 'planes.html', context )



def dashboard(request):

    if request.POST:

        nameusuario = request.user
        usuario = Usuarios.objects.get(fk_user=nameusuario)
        codusuario = usuario.id_usuario

        codigo_plan=request.POST['codigoplan']

        planentreno = Planes.objects.get(id_plan=codigo_plan)
        idhabi = planentreno.id_rango_id

        idarea = planentreno.id_area_id
        area = Areas.objects.get(id_area=idarea)
        nombre_area = getattr(area, "descripcion")

        #sirve para validar desde que sesion se muestra
        diasEntrenados=getattr(planentreno, "dias_entrenados")
        
        #!con base en este se muestra la siguiente sesion, validar
        #! validar que se sion va y mostrar desde esa, con numero de entrenos hechos
        #! si va5 se muestra desde 6

        sesiones = Sesiones.objects.filter(id_plan=codigo_plan).order_by('num_sesiones')
        sesiones2=sesiones[diasEntrenados:]
        #print(sesiones)


        #captura los ids de las sesiones del plan seleccionado
        ids_sesiones = []

        sesionmostrar = 0
        for i in sesiones.values():
            ids_sesiones.append(i['id_sesion'])

            # if(sesionmostrar >= diasEntrenados):
            #     {
            #         ids_sesiones.append(i['id_sesion'])
            #     }
            # sesionmostrar += 1

            #print(i)
            #print(sesiones['id_sesion'])
            #print(i['id_sesion'])
            
            # for m in i.values():
            #     print(i['id_sesion'])
        # print(ids_sesiones)
        
        ids_sesiones=ids_sesiones[diasEntrenados:]
        print(ids_sesiones)



        #sesion a mostar entrenos +1
        
        codigo_sesion=ids_sesiones[0]

        ejercicios = Ejercicios.objects.all()
        sesiones_ejercicio= Sesion_Ejercicio.objects.all()

        duracion_sesiones = []
        #calcular duracion total de las sesiones
        for n in ids_sesiones:
            sesion_ejer = Sesion_Ejercicio.objects.filter(id_sesion=n)

            if(sesion_ejer.exists()):
                #print(sesion_ejer)
                dura=0
                for e in sesion_ejer.values():
                    #print("id_ejercicio:  ")
                    #print(e['id_ejercicios_id'])
                    codigo_ejericio=e['id_ejercicios_id']
                    info_ejercicio = Ejercicios.objects.get(id_ejercicios=codigo_ejericio)
                    #print(info_ejercicio.duracion)
                    dura+=info_ejercicio.duracion

                duracion_sesiones.append(dura)

            else:
                #print("vacio")
                dura=0
                duracion_sesiones.append(dura)

        #print(duracion_sesiones)



        # #ejercicios o sesiones
        # #si ya hizo todos los entrenos del plan no muestra nada
        # if planentreno.dias_entrenados >= totalentrenos:
        #     ejercicios=ejercicios[:0]
        # #si aun no ha hecho todos mandar los dias faltantes de sesiones
        # if planentreno.dias_entrenados < totalentrenos:
        #     ejercicios=ejercicios[:diasrestantes]



        context = {
        "nombre": request.user,
            "iduser": codusuario,
            "area": nombre_area,
            "ejercicios": ejercicios,
            "sesioneshechas":diasEntrenados,
            "codigoplan":codigo_plan,
            "sesiones": sesiones2,
            "idssesiones": ids_sesiones,
            "duraciones": duracion_sesiones,
            "codigosesion": codigo_sesion
        }

        return render(request, 'dashboard.html', context )

    else:
        return render(request, 'planes.html')


def sesion(request):

    if request.POST:
        codigo_plan=request.POST['idplan']
        codigo_sesion=request.POST['idsesion']


        #print(request)

        #!falta capturar el id de usuario, para obtener el codigo de sesion y codigo del plan
        nameusuario = request.user
        usuario = Usuarios.objects.get(fk_user=nameusuario)
        codusuario = usuario.id_usuario


        planentreno = Planes.objects.get(id_plan=codigo_plan)

        idarea = planentreno.id_area_id
        area = Areas.objects.get(id_area=idarea)
        nombre_area = getattr(area, "descripcion")
        
        #captura los ids de los ejercicios de la sesion y el plan seleccionado
        
        sesion_ejer = Sesion_Ejercicio.objects.filter(id_sesion=codigo_sesion)
        ids_ejercicios = []
        ejerci_sesion=[]

        #captura de ejercicios de la sesion
        ejercicios = Ejercicios.objects.all()

        #calcular duracion de cada ejercicio de la sesion
        duracion_ejercicio = []
        
    
        if(sesion_ejer.exists()):
            #print(sesion_ejer)
            dura=0
            for e in sesion_ejer.values():
                #print("id_ejercicio:  ")
                #print(e['id_ejercicios_id'])
                codigo_ejericio=e['id_ejercicios_id']
                ids_ejercicios.append(e['id_ejercicios_id'])


                info_ejercicio = Ejercicios.objects.get(id_ejercicios=codigo_ejericio)
                #print(info_ejercicio.duracion)
                ejerci_sesion.append(info_ejercicio)
                dura=info_ejercicio.duracion
                duracion_ejercicio.append(dura)


        else:
            #print("vacio")
            dura=0
            duracion_ejercicio.append(dura)
        
        #print(duracion_ejercicio)
        #print(ids_ejercicios)
        #print(ejerci_sesion)


        context = {
        "nombre": request.user,
            "apellido": "Abreu",
            #"usuarios": usuarios,
            "iduser": codusuario,
            "area": nombre_area,
            "ejercicios": ejerci_sesion,
            "ids_ejercicios":ids_ejercicios,
            "codigoplan":codigo_plan,
            #"sesiones": sesiones,
            "idsesion": codigo_sesion,
            "duracion": duracion_ejercicio,
            "codigosesion": codigo_sesion
        }
    
        #formulario=DashboardForm()
        
        return render(request, 'sesion.html', context)
    
    else:
        return render(request, 'planes.html')




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

