from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from random import randrange
from .forms import DashboardForm, PlanesForm
from .models import Usuarios
from .models import Planes
from .models import Areas
from .models import Ejercicios, EjerciciosUsuarios
from .models import Rangos
from .models import Sesiones
from .models import Sesion_Ejercicio
from .models import Habilidades
from WorkoutsApp.recomendador import *
from datetime import datetime, date, timedelta
from django.urls import reverse


def index(request):
    return HttpResponse("<h2>Workouts</h2>")

# Create your views here.

def register(request):
    return render(request, 'WorkoutsApp/register.html')

def sesion2(request):

    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)

    print("sesion2 para cuando todo esta listo")
    name=nameusuario
    valor2=datetime.today()
    context = {
        'valor1': name,
        'valor2':valor2

    }
    # if request.POST:

    #     print(request.POST['codigoplan'])

    # formulario=DashboardForm()
    return render(request, 'sesion2.html', context)

def sugerencias(request):
    userconect = request.POST.get('user')

    #authenticate(request, username=username, password=password)

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

def calificaejercicios(request, id):
    print("id que esta llegando a califica ejercicios"+id)

    return redirect('/index')

def aumentasesion(request, valores):
    #recibir array y enviarlo a calificar ejercicio .
    print("entro a aumenta sesion plan#=  "+valores)#+str(valores))

     #captura los ids de los ejercicios de la sesion y el plan seleccionado
    calificaciones = valores.split(",")
    puntajeCalificaciones=calificaciones[2:]

    id=calificaciones[0]

    #aumentar rango
    valorpuntajehabilidad=0.0
    val1=33.0
    val2=70.0
    idrango=1

    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    #usuario.puntaje_habilidades = usuario.puntaje_habilidades+0.1
    valorpuntajehabilidad = usuario.puntaje_habilidades+0.1
    usuario.puntaje_habilidades = usuario.puntaje_habilidades+0.1
    if(valorpuntajehabilidad < val1):
        idrango=1
    elif (valorpuntajehabilidad >= val1 and valorpuntajehabilidad < val2):
        idrango=2
    else:
        idrango=3

    usuario.rango = Rangos.objects.get(id_rango=idrango)
    rangoactual = usuario.rango

    usuario.save()


    infoplan = Planes.objects.get(id_plan=id)
    nuevodiasentrenados= infoplan.dias_entrenados
    infoplan.dias_entrenados = nuevodiasentrenados+0.1
    infoplan.ultima_semana = datetime.today()
    infoplan.save()

     #codigo sesion
    codigo_sesion=calificaciones[1]
    sesion_ejer = Sesion_Ejercicio.objects.filter(id_sesion=codigo_sesion)
    ids_ejercicios = []

    if(sesion_ejer.exists()):
        for e in sesion_ejer.values():
            ids_ejercicios.append(e['id_ejercicios_id'])
    else:
        print("no existen sesiones de este ejercicio")

    #print("ids y calificaciones listas")
    posicion=0
    for ejercicio in ids_ejercicios:
        #print("ejercicio con id: "+str(ids_ejercicios[posicion])+" total puntaje: "+str(puntajeCalificaciones[posicion]))
        ejerci=Ejercicios.objects.get(id_ejercicios=ids_ejercicios[posicion])
        infoEjercicio = EjerciciosUsuarios.objects.get(id_ejercicios=ejerci, id_usuario=usuario.id_usuario)
        infoEjercicio.calificacion = puntajeCalificaciones[posicion]
        infoEjercicio.save()
        posicion+=1

    #aumentar habilidades, 
    areaplan=infoplan.id_area.descripcion
    areaplan=areaplan.lower()
    
    habilidadesUser=Habilidades.objects.get(fk_user=nameusuario)

    if(areaplan == "flexibilidad"):
        habilidadesUser.flexibilidad = habilidadesUser.flexibilidad+0.1
        
    elif(areaplan == "fuerza"):
        habilidadesUser.fuerza = habilidadesUser.fuerza+0.1
        
    elif(areaplan == "resistencia"):
        habilidadesUser.resistencia = habilidadesUser.resistencia+0.1
        
    elif(areaplan == "velocidad"):
        habilidadesUser.velocidad = habilidadesUser.velocidad+0.1
        
    elif(areaplan == "aceleracion"):
        habilidadesUser.aceleracion =habilidadesUser.aceleracion+0.1
      
    elif(areaplan == "agilidad"):
        habilidadesUser.agilidad = habilidadesUser.agilidad+0.1
        
    elif(areaplan == "coordinacion"):
        habilidadesUser.coordinacion = habilidadesUser.coordinacion+0.1
      
    elif(areaplan == "precision"):
        habilidadesUser.precision = habilidadesUser.precision+0.1
       
    else:
        print("area no reconocida")

    habilidadesUser.id_rango = rangoactual

    habilidadesUser.save()

    # #y aumentar puntaje total


    return redirect('/index')

def validaplanes(request):

    print("post post")

    if(request.POST):

        nameusuario = request.user
        usuario = Usuarios.objects.get(fk_user=nameusuario)

        print("request post validada planes ")
        codigoplan=request.POST['codigoplan']
        
        info_plan = Planes.objects.get(id_plan=codigoplan)
        diasEntrenados=getattr(info_plan, "dias_entrenados")
        id_raangoplan=getattr(info_plan, "id_rango")
        id_areaplan=getattr(info_plan, "id_area")
        totalsesiones=getattr(info_plan, "num_sesiones")

        if(diasEntrenados > 0):

            idplan = codigoplan
            
            ejercicioInicio2 = EjerciciosUsuarios.objects.filter(id_rango =id_raangoplan, id_area=id_areaplan, id_usuario=usuario.id_usuario)
            alguno= ejercicioInicio2.order_by('?').first()

            descripcionEjercicio = alguno.descripcion
            areaEjercicio = alguno.id_area
            recomendaciones = recomendadorEjercicios(descripcionEjercicio, areaEjercicio.id_area, usuario.id_rango.id_rango, usuario.id_usuario).tolist()
            #se debe obtener plan
            plan = Planes.objects.get(id_plan = idplan)
            diasentrenados=plan.dias_entrenados
            next_sesion=diasentrenados+1
            crearSesion(plan,next_sesion)

            sesion = Sesiones.objects.get(id_plan=idplan, num_sesiones=next_sesion)
            
            crearSesionesEjercicios(recomendaciones, sesion, usuario)
            print("sale de crear la sesion "+str(next_sesion)+" enviar a dashboard "+str(next_sesion)+" para empezarla")

            return redirect('/workoutsapp/dashboard/'+str(idplan))

        else:
            
            print("crear 1ra primera sesion, porque no tiene, manda a sesion 0")
            idplan = codigoplan

            plan = Planes.objects.get(id_plan = idplan)
            context = {
                'idplan': idplan
                }
            
            return HttpResponseRedirect(reverse('workoutsapp:sesion0', args=[idplan]))
            
            # #sirve pinta bien, pero no cambia url
            # return sesion0(request, idplan)
            # #funciona para pintar
            # return render(request, 'sesion0.html/', context )
            
    return redirect('/index')
    #return render(request, 'validaplanes.html')

def crearplanes(request):
    print("vista crear planes")

    #si 
    formPlanes = PlanesForm(request.POST or None)
    context = {
        'form' : formPlanes
    }
    if request.POST:
        formPlanes = PlanesForm(data=request.POST, instance=request.user)

        if formPlanes.is_valid():

            user = formPlanes.save(commit=False)
            user.save()

            nameusuario = request.user
            usuario = Usuarios.objects.get(fk_user=nameusuario)

            if (Planes.objects.all().exists()):
                id_plan = (Planes.objects.last().id_plan)+1 #
            else:
                print("no existe crear primer valor")
                id_plan=1
            
            id_area = Areas.objects.get(id_area=request.POST.get('id_area'))
            id_usuario = usuario #
            id_rango = usuario.id_rango

            planes = Planes(id_plan=id_plan,
            id_area=id_area,
            id_usuario=id_usuario,
            id_rango=id_rango,
            dias_disponibles=0,
            dias_entrenados=0,
            dias_esta_semana=0,
            num_sesiones=3,
            ultima_semana=date.today()+timedelta(days=-1))
            planes.save()

            return redirect('/workoutsapp/planes/')

    return render(request, 'crearplanes.html', context)

def entrenoslistos(request):
    print("ingreso a entrenos listos")
    nameusuario = request.user
    
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    print(usuario)
    codusuario = usuario.id_usuario
    print(codusuario)
    
    context = {
        "nombre": request.user,
        "apellido": "Abreu",
        "iduser": codusuario,
        "planes": 1,
        "next":date.today()+timedelta(days=-1)
    }
    return render(request, 'entrenoslistos.html', context)

def planes(request):
    print("request planes")

    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    codusuario = usuario.id_usuario

    actualizarEjercicios(usuario.id_usuario)

    planesentreno = Planes.objects.filter(id_usuario=codusuario)

    planesentreno2=[]
    #validar si algun plan tiene todas las sesiones hechas y quitarlo
    if(planesentreno.exists()):
        totalPlanes=0
        totalPlanesHabilitados=0
        for e in planesentreno.values():
            totalsesiones=e['num_sesiones']
            sesioneshechas=e['dias_entrenados']
            ultimoentreno=e['ultima_semana']
            diaactual=datetime.today()
            diaactual2=diaactual.now().date()
            habilitado=False

            if(ultimoentreno < diaactual2):
                print("habilitado")
                habilitado=True
            else:
                print("deshabilitado")
                habilitado=False

            if(sesioneshechas >= totalsesiones):
                print("ya acabo el plan")
            else:
                print("aun le fatla acabar el plan")
                totalPlanes+=1
                if(habilitado==True):
                    print("esta habilitado este plan para hoy, agregarlo")
                    totalPlanesHabilitados+=1
                    idplan=e['id_plan']
                    info_plan = Planes.objects.get(id_plan=idplan)
                    planesentreno2.append(info_plan)

        if(totalPlanes == 0):
            print("no hay planes del usuario, sale a crear un plan")
            return redirect("/workoutsapp/crearplanes/")
        else:
            print("si hay planes")
            if(totalPlanesHabilitados == 0):
                print("no hay planes del usuario, sale a crear un plan o a descansar")
                #HttpResponseRedirect(request, entrenoslistos)
                return redirect ("/workoutsapp/sesion2/")

    else:

        print("no hay planes del usuario")
        return redirect("/workoutsapp/crearplanes/")

    context = {
        "nombre": request.user,
        "apellido": "Abreu",
        "iduser": codusuario,
        "planes": planesentreno2
    }

    return render(request, 'planes.html', context)

def dashboard(request,id):
    print("entro a dashboar codigo plan = "+str(id))

    if(int(id)):
        planentreno = Planes.objects.filter(id_plan=id).exists()
        if(planentreno):
            print("si existe mostrar dashboard con sesion para empezar")
            #return redirect('/workoutsapp/dashboard/'+str(id))

            nameusuario = request.user
            usuario = Usuarios.objects.get(fk_user=nameusuario)
            codusuario = usuario.id_usuario

            codigo_plan=id

            planentreno = Planes.objects.get(id_plan=codigo_plan)
            idhabi = planentreno.id_rango_id

            idarea = planentreno.id_area_id
            area = Areas.objects.get(id_area=idarea)
            nombre_area = getattr(area, "descripcion")

            #sirve para validar desde que sesion se muestra
            diasEntrenados=getattr(planentreno, "dias_entrenados")
            
            #con base en este se muestra la siguiente sesion
            # validar que se sion va y mostrar desde esa, con numero de entrenos hechos
            # si va5 se muestra desde 6

            sesiones = Sesiones.objects.filter(id_plan=codigo_plan).order_by('num_sesiones')
            sesiones2=sesiones[diasEntrenados:]

            #captura los ids de las sesiones del plan seleccionado
            ids_sesiones = []

            for i in sesiones2.values():
                ids_sesiones.append(i['id_sesion'])

            #sesion actual
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
                        codigo_ejericio=e['id_ejercicios_id']
                        info_ejercicio = Ejercicios.objects.get(id_ejercicios=codigo_ejericio)
                        dura+=info_ejercicio.duracion

                    duracion_sesiones.append(dura)

                else:
                    dura=0
                    duracion_sesiones.append(dura)

            color=["border-bottom-success", "border-bottom-primary", "border-bottom-secondary"]

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
                "codigosesion": codigo_sesion,
                "colors":color
            }

            return render(request, 'dashboard.html/', context )

        else:
            print("no existe mandar al index")
            return redirect('/index')
    else:
        print("no existe url mandar al index")
        return redirect('/index')

def sesion(request):

    if request.POST:
        codigo_plan=request.POST['idplan']
        codigo_sesion=request.POST['idsesion']

        nameusuario = request.user
        usuario = Usuarios.objects.get(fk_user=nameusuario)
        codusuario = usuario.id_usuario
        
        planentreno = Planes.objects.get(id_plan=codigo_plan)
        numSesion = planentreno.dias_entrenados

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
            dura=0
            for e in sesion_ejer.values():
                codigo_ejericio=e['id_ejercicios_id']
                ids_ejercicios.append(e['id_ejercicios_id'])


                info_ejercicio = Ejercicios.objects.get(id_ejercicios=codigo_ejericio)
                ejerci_sesion.append(info_ejercicio)
                dura=info_ejercicio.duracion
                duracion_ejercicio.append(dura)


        else:
            dura=0
            duracion_ejercicio.append(dura)

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
            "codigosesion": codigo_sesion,
            "numSesion": numSesion+1
        }
    
        #formulario=DashboardForm()
        
        return render(request, 'sesion.html', context)
    
    else:
        return redirect('/index')

def sesion0(request, id):
    if(request.POST):
        print("POST SESION0")
    if(request.GET):
        print("GET SESION0")
    
    print("entro a sesion del plan  "+ str(id))
    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)

    ejercicios1=EjerciciosUsuarios.objects.all().filter(id_rango = usuario.id_rango, id_usuario=usuario.id_usuario).values()

    ejercicios = seleccionarEjercicios(EjerciciosUsuarios.objects.all().filter(id_rango = usuario.id_rango, id_usuario=usuario.id_usuario))

    idplan = id
    num_sesiones = 1
    context = {
        'ejercicios': ejercicios,
        'idplan':idplan
    }

    if request.POST and request.POST.get('radio') != None:
        print(" post sesion 0 ")
        idplan = request.POST['idplan']

        ejercicio=request.POST.get('radio')
        
        ejercicioInicio = EjerciciosUsuarios.objects.get(id_ejercicios_usuarios = ejercicio, id_usuario=usuario.id_usuario)
        descripcionEjercicio = ejercicioInicio.descripcion
        areaEjercicio = ejercicioInicio.id_area

        recomendaciones = recomendadorEjercicios(descripcionEjercicio, areaEjercicio.id_area, usuario.id_rango.id_rango, usuario.id_usuario).tolist()

        sesiones= Sesiones.objects.filter(id_plan=idplan, num_sesiones=num_sesiones).order_by('num_sesiones')

         #se debe obtener plan
        plan = Planes.objects.get(id_plan = idplan)


        if(sesiones.exists()):
            return redirect('/workoutsapp/dashboard/'+str(idplan))
        else:

            crearSesion(plan,num_sesiones)

            sesion = Sesiones.objects.get(id_plan=idplan, num_sesiones=num_sesiones)

            crearSesionesEjercicios(recomendaciones, sesion, usuario)

            return redirect('/workoutsapp/dashboard/'+str(idplan))

    return render(request, 'sesion0.html', context)

def recomendadorEjercicios(descripcion, area, id_rango, id_usuario):
    EjerciciosDF, cosine_sim, indices = recomendador(id_usuario)
    ind=2
    conjuntoEjercicios = get_recommendations(EjerciciosDF, descripcion, id_rango, area, cosine_sim, indices)
    return conjuntoEjercicios

def crearSesion(id_plan, numsesion):
    sesion = Sesiones(id_plan=id_plan, fecha=datetime.today(), num_sesiones=numsesion)
    sesion.save()

def crearSesionesEjercicios(ejercicios, sesion, id_user):
    for ejercicio in ejercicios:
        ejercicioInstancia = EjerciciosUsuarios.objects.get(id_ejercicios = ejercicio, id_usuario=id_user)
        calificacicion1=ejercicioInstancia.calificacion
        bestSesion=0
        fecha1=datetime.today()
        sesionEjercicio = Sesion_Ejercicio(id_sesion=sesion, id_ejercicios=ejercicioInstancia.id_ejercicios,calificacion=calificacicion1, mejor_sesion=bestSesion, fecha=fecha1 )
        sesionEjercicio.save()

def seleccionarEjercicios(array):
    ejercicios = []
    while(len(ejercicios) <= 2):
        posicion = randrange(array.count())
        try:
            if ejercicios.index(array[posicion]):
                pass
        except ValueError:
            ejercicios.append(array[posicion])
    return ejercicios

def actualizarEjercicios(id_user):
    #!usuario, ver si el ejercicio no esta y agregarlo, o si esta dejarlo.
    #nameusuario = request.user
    usuario = Usuarios.objects.get(id_usuario=id_user)
    codusuario = usuario.id_usuario

    ejerciciosOriginales=Ejercicios.objects.all()
    ejerciciosUsers=EjerciciosUsuarios.objects.filter(id_usuario=codusuario)

    if(ejerciciosOriginales.exists()):
        if(ejerciciosUsers.exists()):
            print("existen ambos ejercicios. validar si hay alguno nuevo y actualizar")
            for o in ejerciciosOriginales.values():
                #recorrer for original con cada valor, luego con cada valor recorrer for users
                #  viendo si existe o no, y si no existe agregarlo
                contador=0
                ejercicioOr=o['id_ejercicios']
                for c in ejerciciosUsers.values():

                    ejercicioUs=c['id_ejercicios_id']

                    if(ejercicioOr == ejercicioUs):
                        contador+=1

                if(contador == 0):
                    #no existe agregarlo con el id usuario
                    print("no existe agregarlo con id usuario")
                    idnuevo=EjerciciosUsuarios.objects.last().id_ejercicios_usuarios
                    idnuevo=int(idnuevo)+1

                    ejercicioAdd=EjerciciosUsuarios(

                        id_ejercicios_usuarios=idnuevo,
                        id_ejercicios= Ejercicios.objects.get(id_ejercicios=o['id_ejercicios']),
                        descripcion= o['descripcion'],
                        id_rango= Rangos.objects.get(id_rango=o['id_rango_id']),
                        duracion= o['duracion'],
                        repeticiones= o['repeticiones'],
                        calificacion= o['calificacion'],
                        explicacion= o['explicacion'],
                        id_area= Areas.objects.get(id_area=o['id_area_id']),
                        link_entreno= o['link_entreno'],
                        id_usuario= usuario)
                    ejercicioAdd.save()

                    print("actualizo ejercicios, creo ejercicios en bd que no existia")
                    
        else:
            print("no existen ejercicios del usuario agregarlos todos para el id user")
            ejercopia= EjerciciosUsuarios.objects.last()
            hayejercicios=0
            
            if(ejercopia is None):
                print("es none no hay nada")
                hayejercicios=0
                idnuevo=0
            else:
                print("no es none ya hay algo")
                hayejercicios=1
                idnuevo=EjerciciosUsuarios.objects.last().id_ejercicios_usuarios
                
            for o in ejerciciosOriginales.values():

                idnuevo=int(idnuevo)+1

                ejercicioAdd=EjerciciosUsuarios(
                    id_ejercicios_usuarios=idnuevo,
                    id_ejercicios= Ejercicios.objects.get(id_ejercicios=o['id_ejercicios']),
                    descripcion= o['descripcion'],
                    id_rango= Rangos.objects.get(id_rango=o['id_rango_id']),
                    duracion= o['duracion'],
                    repeticiones= o['repeticiones'],
                    calificacion= o['calificacion'],
                    explicacion= o['explicacion'],
                    id_area= Areas.objects.get(id_area=o['id_area_id']),
                    link_entreno= o['link_entreno'],
                    id_usuario= usuario)

                ejercicioAdd.save()

                print("creo ejercicios en bd por primera vez")
    else:
        print("no existen ejercicios originales porfavor cree ejercicios ")
