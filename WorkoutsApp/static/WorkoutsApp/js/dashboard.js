//alert("todo se ejecuta mi papusito")


//globals
var local = localStorage;
var id_plan="";
var id_sesion="";
var estadoPlan = false;
var estadoSesion = false;


window.onload = function()
{

  validarFechas();
  duraciones();
  mostrar();

};


//valida si hay una sesion corriendo para cargar redirigir a la sesion en curso
function valida_sesion_iniciada()
{

  //validar si esta en alguna sesion
  id_plan = buscarlocal('id_plan');
  id_sesion = buscarlocal('id_sesion');


  if(id_plan === null && id_sesion === null)
  {
    console.log("no existe ninguno en local");
    estadoPlan = false;
    estadoSesion = false;

  }else if(id_plan =! null && id_sesion === null)
  {
    console.log("solo existe el plan, mas no la sesion");
    console.log(id_plan);
    estadoPlan = true;
    estadoSesion = false;

  }else
  {
    console.log("existen las dos en el local");
    console.log(id_plan);
    console.log(id_sesion);
    estadoPlan = true;
    estadoSesion = true;
  }
}

function mostrar()
{
  valida_sesion_iniciada();

  if(estadoPlan != false && estadoSesion != false)
  {
    console.log("plan y sesion estan iniciado, cargar sesion del plan actual");
    id_plan = buscarlocal('id_plan');
    id_sesion = buscarlocal('id_sesion');
  }else if(estadoPlan =! false && estadoSesion === false)
  {
    console.log("plan iniciado, pero sesion no esta seleccionada, cargar sesiones ");
    id_plan = buscarlocal('id_plan');
  }
  else
  {
    console.log("ningun plan seleccionado, seleccione un plan, cargar planes");
  }
}

//almacena datos en localstorage para no perder al recargar pagina
function almacenarlocal(clave, valor)
{
  local.setItem(clave, valor);
  console.log("guardo");

  //borrar
  //localStorage.removeItem('nombre');
  //limpiar
  //localStorage.clear();

}

function buscarlocal(clave)
{
  var info = local.getItem(clave);
  return info;
}


function validarFechas()
{

  var sesiones = document.getElementById('asesiones').innerText;
  if( sesiones != null)
  {
    // console.log("si existe")
    // console.log(sesiones)


    array_sesiones = sesiones.split(',')


    for (let step = 0; step < array_sesiones.length; step++)
    {
      if(step==0)
      {
        var fecha = new Date();
        document.getElementById('fecha0').innerHTML += Fecha(fecha);
      }
      else
      {
        var numerofecha="fecha"
        numerofecha+=step;
        var fecha2 = new Date();
        var fecha3 = sumarDias(fecha2, step);

        document.getElementById(numerofecha).innerHTML += Fecha(fecha3)
      }

    }

    document.getElementById("asesiones").style.display = "none";
  }


}



function todo()
    {
    var fecha = new Date();
    var numdia = fecha.getDate();
    var dia = fecha.getDay();
    var mes = fecha.getMonth();
    var añito = fecha.getYear()+1900;
    var ddisponibles = 5;
    var diasestasemana = 2;
    var diasentrenados = 7;
    var totalentrenos = 10;
    var mostrar = false;

    if(diasentrenados >= totalentrenos)
    {
        document.write("NO TIENES ENTRENOS, YA LOS HICISTE TODOS, PASAR AL SIGUIENTE NIVEL");
        mostrar=false;
        document.getElementById("entrenos").style.display="none";
    }
    if(diasentrenados < totalentrenos)
    {
        document.write("AUN TE FALTAN ENTRENOS ");
        mostrar = true;
        document.getElementById("entrenos").style.display="";
        
    }
    }
/*       documente.getElementById("most").value=true; */
    /* document.getElementById("entrenos").innerHTML = mostrar; */



/* Función que suma o resta días a una fecha, si el parámetro
    días es negativo restará los días*/
function sumarDias(fecha, dias)
  {
    fecha.setDate(fecha.getDate() + dias);
    return fecha;
  }

function Fecha(fecha)
{
meses = new Array("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
data = fecha;

index = data.getMonth();
diasemana=new Array("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo");

indexday =  data.getDay();
if (indexday == 0)
indexday = 7;

any = data.getYear();
if (any < 1900)
  any = 1900 + any;

fechafinal=""
fechafinal+=(diasemana[indexday-1]+ "," + ' '+data.getDate()+ " de " + meses[index] + " de " + any);

return fechafinal;
}

//ejercutar funcion al cargar pagiina
//document.addEventListener('DOMContentLoaded',hola, false);


function duraciones()
{
  console.log("duraciones");
  var valores = document.getElementById('aduracion').innerText;
  console.log("valores duraciones")
  console.log(valores)
  //alert(typeof(valores));
  
  if( valores != null)
  {
    // console.log("si existe")
    // console.log(valores)
    var durac = "duracion0"
    var valor="";
    //ingreso un solo numero
    if(valores.length == 3)
    {
      valor=valores.slice(1,2);
    }else if(valores.length > 3)
    {
      valor=valores.slice(1,valores.length-1);
    }else{
      valor="";
    }
    document.getElementById(durac).innerHTML = valor;
    

    // array_valores = valores.split(',');

    // for (var i=0; i<array_valores.length; i++)
    // {
    //   var durac = "duracion"
    //   if(i == 0)
    //   {
    //     durac+=i;
    //     document.getElementById(durac).innerHTML = array_valores[i].substr(1);
    //     //console.log(array_valores[i].substr(1));
    //   }
    //   else if(i == (array_valores.length - 1))
    //   {
    //     durac+=i;
    //     document.getElementById(durac).innerHTML = array_valores[i].slice(0,-1);
    //     //console.log(array_valores[i].slice(0,-1));
    //   }
    //   else
    //   {
    //     durac+=i;
    //     document.getElementById(durac).innerHTML = array_valores[i];
    //     //console.log(array_valores[i]);
    //   }
    // }

    document.getElementById("aduracion").style.display = "none";


  }else
  {
    console.log("no existe")
  }

}


//saber que evento sucede y capturarlo
function conocerEvento(e) {

	var evento = e || window.event;

		//document.getElementById("evento").value = e.type;

    // console.log("evento");
    // console.log(e);

    if(evento.type == "click")
    {
      console.log("nombre del click");
      console.log(evento.path[0].id);

      var nombreclick=evento.path[0].id;


      //iniciar
      if(nombreclick.substr(0,7) == "iniciar")
      {
        //alert("click");
        //var id=nombreclick.substr(7);
        //console.log("comienza valor");
        //console.log(nombreclick.substr(8));
        //alert("empezo entreno");

        id_sesion = document.getElementById("idsesion").innerText;
        //console.log(id_sesion);
        almacenarlocal('id_plan', id_plan);
        almacenarlocal('id_sesion', id_sesion);

      }




    }


    // switch(evento.type) {
    //   case 'mouseover':
    //     this.style.borderColor = 'black';
    //     break;
    //   case 'mouseout':
    //     this.style.borderColor = 'silver';
    //     break;
    // }

}


document.onclick = conocerEvento;
document.onmousedown = conocerEvento;
document.onmouseup = conocerEvento;
document.ondblclick = conocerEvento;
document.onkeydown = conocerEvento;
document.onmouseover = conocerEvento;