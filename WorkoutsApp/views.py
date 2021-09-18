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

    usuarios = Usuarios.objects.all()

    #usuario= Usuarios.objects.get(id_usuario=iduser)

    #!falta capturar el id del usuario con el name de usuario, este es de prueba
    iduser=1

    #iduser2=request.POST.get('id_usuario')
    #idusuario= Usuarios.objects.get(id_usuario=iduser)

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
        "planes": planesentreno
    }

    return render(request, 'planes.html', context )



def dashboard(request):

    if request.POST:

        iduser=1

        #if request.POST:
        #   print(request.POST['codigoplan'])

        codigo_plan=request.POST['codigoplan']


        planentreno = Planes.objects.get(id_plan=codigo_plan)
        idhabi = planentreno.id_rango_id

        idarea = planentreno.id_area_id
        area = Areas.objects.get(id_area=idarea)
        nombre_area = getattr(area, "descripcion")

        diasEntrenados=getattr(planentreno, "dias_entrenados")
        #!con base en este se muestra la siguiente sesion

        sesiones = Sesiones.objects.filter(id_plan=codigo_plan)
        #print(Sesiones.objects.order_by('num_sesion'))
        #sesionesasc = sesiones.order_by('num_sesion')
        #sesionesdesc = sesiones.order_by('-num_sesion')
        #print(sesionesasc)
        #print(sesionesdesc)

        #print(sesiones)
        #captura los ids de las sesiones del plan seleccionado
        ids_sesiones = []

        for i in sesiones.values():
            #print(i)
            #print(sesiones['id_sesion'])
            #print(i['id_sesion'])
            ids_sesiones.append(i['id_sesion'])
            # for m in i.values():
            #     print(i['id_sesion'])
        #print(ids_sesiones)



        #! falta capturar codigo de la sesion que va a realizar, o sea la primera
        codigo_sesion=1

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

        print(duracion_sesiones)



        #obtener info sesion ejercicios
        #ejercicios filtrados por habilidad, debe ser por sesion o como se escoja
        #ejercicios = Ejercicios.objects.filter(id_rango=idhabi)




        #dias que entreno, para ver cuantas sesiones mostrar

        hoy = datetime.today().isoweekday()
        #diasrestantes=7-hoy
        diasrestantes=4
        totalentrenos=5


        #se obtiene toda la info de las tablas de la BD
        #usuarios = Usuarios.objects.all()



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
            #"usuarios": usuarios,
            "iduser": iduser,
            "area": nombre_area,
            "ejercicios": ejercicios,
            "diasrestantes":diasrestantes,
            "codigoplan":codigo_plan,
            "sesiones": sesiones,
            "idssesiones": ids_sesiones,
            "duraciones": duracion_sesiones,
            "codigosesion": codigo_sesion
        }

        return render(request, 'dashboard.html', context )

    else:
        return render(request, 'planes.html')


def sesion(request):

    #print(request)

    #!falta capturar el id de usuario, para obtener el codigo de sesion y codigo del plan
    iduser=1
    codigo_plan=1
    codigo_sesion=1
    nombre_area="area aqui"


    # if request.POST:

    #     #print(request.POST['codigoplan'])
    #     print(request.POST['idsesion'])


    #codigoplan=request.POST['codigoplan']
    idsesion=request.POST['idsesion']

    
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
        "iduser": iduser,
        "area": nombre_area,
        "ejercicios": ejerci_sesion,
        "ids_ejercicios":ids_ejercicios,
        "codigoplan":codigo_plan,
        #"sesiones": sesiones,
        "idsesion": idsesion,
        "duracion": duracion_ejercicio,
        "codigosesion": codigo_sesion
    }
 
    #formulario=DashboardForm()
    
    return render(request, 'sesion.html', context)




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

