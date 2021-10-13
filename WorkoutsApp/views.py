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

    print("sesion2 para cuando todo esta listo")
    print(request)

    # if request.POST:

    #     print(request.POST['codigoplan'])

    # formulario=DashboardForm()
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

def calificaejercicios(request, id):
    print("id que esta llegando a califica ejercicios"+id)
    #print("entro a aumenta sesion plan#=  "+str(id))

    # nameusuario = request.user
    # usuario = Usuarios.objects.get(fk_user=nameusuario)
    
    # infoplan = Planes.objects.get(id_plan=id)

    # nuevodiasentrenados= infoplan.dias_entrenados
    # infoplan.dias_entrenados = nuevodiasentrenados+1
    # infoplan.save()

    return redirect('/index')

def aumentasesion(request, valores):
    #recibir array y enviarlo a calificar ejercicio .
    print("entro a aumenta sesion plan#=  "+valores)#+str(valores))

     #captura los ids de los ejercicios de la sesion y el plan seleccionado
    calificaciones = valores.split(",")
    #print(calificaciones)
    #print(calificaciones[2:])
    puntajeCalificaciones=calificaciones[2:]

    id=calificaciones[0]
    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    
    infoplan = Planes.objects.get(id_plan=id)

    nuevodiasentrenados= infoplan.dias_entrenados
    infoplan.dias_entrenados = nuevodiasentrenados+1
    infoplan.ultima_semana = datetime.today()
    infoplan.save()

     #codigo sesion
    codigo_sesion=calificaciones[1]
    sesion_ejer = Sesion_Ejercicio.objects.filter(id_sesion=codigo_sesion)
    ids_ejercicios = []

    if(sesion_ejer.exists()):
        for e in sesion_ejer.values():
            ids_ejercicios.append(e['id_ejercicios_id'])
        print("ids ejerciciosejercicios")
        print(ids_ejercicios)
    else:
        print("vacio")
        print(ids_ejercicios)
    

    print("ids y calificaciones listas")
    posicion=0
    for ejercicio in ids_ejercicios:
        
        print("ejercicio con id: "+str(ids_ejercicios[posicion])+" total puntaje: "+str(puntajeCalificaciones[posicion]))
        ejerci=Ejercicios.objects.get(id_ejercicios=ids_ejercicios[posicion])
        infoEjercicio = EjerciciosUsuarios.objects.get(id_ejercicios=ejerci, id_usuario=usuario.id_usuario)
        infoEjercicio.calificacion = puntajeCalificaciones[posicion]
        infoEjercicio.save()
        posicion+=1


    return redirect('/index')

def validaplanes(request):

    print("post post")
    #print(request.POST)

    if(request.POST):

        nameusuario = request.user
        usuario = Usuarios.objects.get(fk_user=nameusuario)

        print("request validador de planes ")
        print(request.POST['codigoplan'])
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
            recomendaciones = recomendadorEjercicios(descripcionEjercicio, areaEjercicio.id_area, usuario.id_rango.id_rango).tolist()
            #se debe obtener plan
            plan = Planes.objects.get(id_plan = idplan)
            diasentrenados=plan.dias_entrenados
            next_sesion=diasentrenados+1
            crearSesion(plan,next_sesion)

            sesion = Sesiones.objects.get(id_plan=idplan, num_sesiones=next_sesion)
            
            crearSesionesEjercicios(recomendaciones, sesion, usuario)
            print("sale de crear la sesion "+str(next_sesion)+" enviar a dashboard "+str(next_sesion)+" para empezarla")


            #return redirect('/index')
            return redirect('/workoutsapp/dashboard/'+str(idplan))


            # print("ya empezo el plan, a sesion 0 con un ejercicio anterior")
            # #return render(request, 'index.html')

            # crearSesion(codigoplan,diasEntrenados)
            context = {
                'idplan': codigoplan
                }

            print(context)
            #return redirect('/workoutsapp/dashboard/'+str(codigoplan))

            
        else:
            
            print("crear 1ra primera sesion, porque no tiene, manda a sesion 0")
            idplan = codigoplan

            plan = Planes.objects.get(id_plan = idplan)
            context = {
                'idplan': idplan
                }
            print(context)
            print("sale")
            
            return HttpResponseRedirect(reverse('workoutsapp:sesion0', args=(idplan)))
            
            #sirve pinta bien, pero no cambia url
            return sesion0(request, idplan)
            #funciona para pintar
            return render(request, 'sesion0.html/', context )
            
    return redirect('/index')
    #return render(request, 'validaplanes.html')

def crearplanes(request):
    print("vista crear planes")
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
            id_rango = usuario.id_rango #
            # dias_disponibles = request.POST.get('dias_disponibles')
            # dias_entrenados = request.POST.get('dias_entrenados')
            # dias_esta_semana = request.POST.get('dias_esta_semana')
            # num_sesiones = request.POST.get('num_sesiones')
            # ultima_semana = request.POST.get('ultima_semana')

            print("abre datos crear planes")
            print(id_plan)
            print(id_area)
            print(id_usuario)
            print(id_rango)
            # print(dias_disponibles)
            # print(dias_entrenados)
            # print(dias_esta_semana)
            # print(num_sesiones)
            # print(ultima_semana)
            print("cierra datos crear planes")

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
        #"usuarios": usuarios,
        "iduser": codusuario,
        #"planes": planesentreno2
        "planes": 1,
        "next":date.today()+timedelta(days=-1)
    }
    return render(request, 'entrenoslistos.html', context)

def planes(request):
    print("request planes")
    #print(request)

    #se obtiene toda la info de las tablas de la BD

    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    codusuario = usuario.id_usuario

    actualizarEjercicios(usuario.id_usuario)
    #print("ya paso por actualizar ejercicios")


    planesentreno = Planes.objects.filter(id_usuario=codusuario)

    planesentreno2=[]
    #ids_planes=[]
    #validar si algun plan tiene todas las sesiones hechas y quitarlo
    if(planesentreno.exists()):
        totalPlanes=0
        totalPlanesHabilitados=0
        for e in planesentreno.values():
            #print("id_ejercicio:  ")
            #print(e['id_ejercicios_id'])
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
                return redirect("/workoutsapp/crearplanes/")
                #!crear vista de que ya entreno hoy

    else:

        print("no hay planes del usuario")
        return redirect("/workoutsapp/crearplanes/")
        return redirect("crearplanes.html")
        #return render(request, "crearplanes.html")

    context = {
        "nombre": request.user,
        "apellido": "Abreu",
        #"usuarios": usuarios,
        "iduser": codusuario,
        "planes": planesentreno2
    }

    return render(request, 'planes.html', context)

def dashboard(request,id):
    print("entro a dashboar codigo plan = "+str(id))

    if(int(id)):
        print("es numerico validar si existe esa sesion")
        planentreno = Planes.objects.filter(id_plan=id).exists()
        #planentreno = Planes.objects.get(id_plan=int(id))
        print(planentreno)
        print(id)
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

            # if(diasEntrenados == 0):
            #     print("crear primera sesion, porque no tiene")
            #     return render(request, 'sesion0.html')
            # else:
            #     print("capturar la sesion anterior y escoger un ejercicio para crear la sgt sesion")



            # validar que se sion va y mostrar desde esa, con numero de entrenos hechos
            # si va5 se muestra desde 6

            sesiones = Sesiones.objects.filter(id_plan=codigo_plan).order_by('num_sesiones')
            sesiones2=sesiones[diasEntrenados:]
            print(sesiones2)


            #captura los ids de las sesiones del plan seleccionado
            ids_sesiones = []

            for i in sesiones2.values():
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
            print(ids_sesiones)
            print("ids Sesiones")
            print(len(sesiones2))
            

            #ids_sesiones=ids_sesiones[diasEntrenados:]
            print(ids_sesiones)
            #print(ids_sesiones)

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





    # if request.POST:

    #     nameusuario = request.user
    #     usuario = Usuarios.objects.get(fk_user=nameusuario)
    #     codusuario = usuario.id_usuario

    #     codigo_plan=request.POST['idplan']

    #     planentreno = Planes.objects.get(id_plan=codigo_plan)
    #     idhabi = planentreno.id_rango_id

    #     idarea = planentreno.id_area_id
    #     area = Areas.objects.get(id_area=idarea)
    #     nombre_area = getattr(area, "descripcion")

    #     #sirve para validar desde que sesion se muestra
    #     diasEntrenados=getattr(planentreno, "dias_entrenados")
        
    #     #con base en este se muestra la siguiente sesion

    #     # if(diasEntrenados == 0):
    #     #     print("crear primera sesion, porque no tiene")
    #     #     return render(request, 'sesion0.html')
    #     # else:
    #     #     print("capturar la sesion anterior y escoger un ejercicio para crear la sgt sesion")
    #     #     #!llamar al metodo de crear sesion con una sesion anterior


    #     # validar que se sion va y mostrar desde esa, con numero de entrenos hechos
    #     # si va5 se muestra desde 6

    #     sesiones = Sesiones.objects.filter(id_plan=codigo_plan).order_by('num_sesiones')
    #     sesiones2=sesiones[diasEntrenados:]
    #     #print(sesiones)


    #     #captura los ids de las sesiones del plan seleccionado
    #     ids_sesiones = []

    #     for i in sesiones.values():
    #         ids_sesiones.append(i['id_sesion'])

    #         # if(sesionmostrar >= diasEntrenados):
    #         #     {
    #         #         ids_sesiones.append(i['id_sesion'])
    #         #     }
    #         # sesionmostrar += 1

    #         #print(i)
    #         #print(sesiones['id_sesion'])
    #         #print(i['id_sesion'])

    #         # for m in i.values():
    #         #     print(i['id_sesion'])
    #     # print(ids_sesiones)

    #     ids_sesiones=ids_sesiones[diasEntrenados:]
    #     print(ids_sesiones)

    #     #sesion actual
    #     codigo_sesion=ids_sesiones[0]

    #     ejercicios = Ejercicios.objects.all()
    #     sesiones_ejercicio= Sesion_Ejercicio.objects.all()

    #     duracion_sesiones = []
    #     #calcular duracion total de las sesiones
    #     for n in ids_sesiones:
    #         sesion_ejer = Sesion_Ejercicio.objects.filter(id_sesion=n)

    #         if(sesion_ejer.exists()):
    #             #print(sesion_ejer)
    #             dura=0
    #             for e in sesion_ejer.values():
    #                 #print("id_ejercicio:  ")
    #                 #print(e['id_ejercicios_id'])
    #                 codigo_ejericio=e['id_ejercicios_id']
    #                 info_ejercicio = Ejercicios.objects.get(id_ejercicios=codigo_ejericio)
    #                 #print(info_ejercicio.duracion)
    #                 dura+=info_ejercicio.duracion

    #             duracion_sesiones.append(dura)

    #         else:
    #             #print("vacio")
    #             dura=0
    #             duracion_sesiones.append(dura)

    #     #print(duracion_sesiones)



    #     # #ejercicios o sesiones
    #     # #si ya hizo todos los entrenos del plan no muestra nada
    #     # if planentreno.dias_entrenados >= totalentrenos:
    #     #     ejercicios=ejercicios[:0]
    #     # #si aun no ha hecho todos mandar los dias faltantes de sesiones
    #     # if planentreno.dias_entrenados < totalentrenos:
    #     #     ejercicios=ejercicios[:diasrestantes]

    #     color=["border-bottom-success", "border-bottom-primary", "border-bottom-secondary"]

    #     context = {
    #     "nombre": request.user,
    #         "iduser": codusuario,
    #         "area": nombre_area,
    #         "ejercicios": ejercicios,
    #         "sesioneshechas":diasEntrenados,
    #         "codigoplan":codigo_plan,
    #         "sesiones": sesiones2,
    #         "idssesiones": ids_sesiones,
    #         "duraciones": duracion_sesiones,
    #         "codigosesion": codigo_sesion,
    #         "colors":color
    #     }

    #     return render(request, 'dashboard.html', context )

    # else:
    #     return redirect('/index')

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
        return redirect('/index')

def sesion0(request, id):
    if(request.POST):
        print("POST SESION0")
    if(request.GET):
        print("GET SESION0")
    
    print("entro a sesion del plan  "+ str(id))
    nameusuario = request.user
    usuario = Usuarios.objects.get(fk_user=nameusuario)
    
    #print(Ejercicios.objects.all().filter(id_rango = usuario.id_rango).values())
    print(request)
    print("ejercicios filtrados")
    ejercicios1=EjerciciosUsuarios.objects.all().filter(id_rango = usuario.id_rango, id_usuario=usuario.id_usuario).values()
    print(list(ejercicios1))
    ejercicios = seleccionarEjercicios(EjerciciosUsuarios.objects.all().filter(id_rango = usuario.id_rango, id_usuario=usuario.id_usuario))
    #ejercicios = seleccionarEjercicios(Ejercicios.objects.all().filter(id_rango = usuario.id_rango).values())
    
    if(ejercicios):
        print("si existe usuario")
    else:
        print("no existe usuario")
    
    #obtener el id del plan y num_sesion
    print("codigo del plan que llega en sesion 0")

    #print(idplan)
    idplan = id
    num_sesiones = 1
    context = {
        'ejercicios': ejercicios,
        'idplan':idplan
    }
    #print(context)
    print("antes del post")
    

    if request.POST and request.POST.get('radio') != None:
        print("codigo plan del que llega post")
        print(request.POST['idplan'])
        idplan = request.POST['idplan']

        ejercicio=request.POST.get('radio')
        print(ejercicio)

        
        ejercicioInicio = EjerciciosUsuarios.objects.get(id_ejercicios_usuarios = ejercicio, id_usuario=usuario.id_usuario)
        descripcionEjercicio = ejercicioInicio.descripcion
        areaEjercicio = ejercicioInicio.id_area
        recomendaciones = recomendadorEjercicios(descripcionEjercicio, areaEjercicio.id_area, usuario.id_rango.id_rango).tolist()
        #se debe obtener plan
        plan = Planes.objects.get(id_plan = idplan)
        crearSesion(plan,num_sesiones)

        sesion = Sesiones.objects.get(id_plan=idplan, num_sesiones=num_sesiones)
        
        
        crearSesionesEjercicios(recomendaciones, sesion, usuario)
        print(recomendaciones)
        print("sale de crear la sesion 1 enviar a dashboard para empezarla")

        #return redirect('/index')
        return redirect('/workoutsapp/dashboard/'+str(idplan))

    print("sale a mostrar vista ejercicios sesion0")
    
    return render(request, 'sesion0.html', context)

def recomendadorEjercicios(descripcion, area, id_rango):

    EjerciciosDF, cosine_sim, indices = recomendador()
    # print(EjerciciosDF['id_rango_id'])
    ind=2
    #titulo2 = str(Entrenos.iloc[1]['area']['intensidad'])
    print("seleccionaste: "+ descripcion+ " y tu recomendaciones son: ")
    print("nivel: "+ str(id_rango)+ " area: "+ str(area))
    conjuntoEjercicios = get_recommendations(EjerciciosDF, descripcion, id_rango, area, cosine_sim, indices)
    return conjuntoEjercicios

def crearSesion(id_plan, numsesion):
    sesion = Sesiones(id_plan=id_plan, fecha=datetime.today(), num_sesiones=numsesion)
    sesion.save()

def crearSesionesEjercicios(ejercicios, sesion, id_user):
    for ejercicio in ejercicios:
        ejercicioInstancia = EjerciciosUsuarios.objects.get(id_ejercicios = ejercicio, id_usuario=id_user)
        print(ejercicioInstancia)
        print(sesion)
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
                #print(o['id_rango_id'])

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
