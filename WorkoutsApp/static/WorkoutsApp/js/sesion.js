//alert("Sesionones manimoto");


//globals
var local = localStorage;

//localstorage
var id_plan="";
var id_sesion="";
var estadoPlan = false;
var estadoSesion = false;


//tiempos
let tiempoRef = Date.now();
let cronometrar = false;
let acumulado = 0;
let totalDuracionEntreno=0;

var btnComienza = "comienza";
var btnFin = "fin";
var divEjercicio = "ejercicio";
var divTiempos = "tiempos";
var btnPlay = "play";
var btnPause = "pause";
var btnReset = "reset";




window.onload = function()
{
    primero();
    mostrar();

};


//almacena datos en localstorage para no perder al recargar pagina
function almacenarlocal(clave, valor){
  local.setItem(clave, valor);
}

function buscarlocal(clave)
{
  var info = local.getItem(clave);
  return info;
}

function borrarlocal(clave)
{
  console.log("entro a borrar");
  //var info = local.getItem(clave);

  //borrar
  localStorage.removeItem(clave);
  //limpiar
  //localStorage.clear();
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
  }
  else
  {
    console.log("ningun plan seleccionado, seleccione un plan, cargar planes");
  }
}

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

//tiempos
function iniciar()
{
  cronometrar = true;
}

function pausar() {
  cronometrar = false;
}

function reiniciar() {
  acumulado = 0;
}

setInterval(() =>
{
  let tiempo = document.getElementById("tiempo")
  if (cronometrar) {
    acumulado += Date.now() - tiempoRef;
  }
  tiempoRef = Date.now();
  tiempo.innerHTML = formatearMS(acumulado);
  }, 1000 / 60);

function formatearMS(tiempo_ms)
{
  let MS = tiempo_ms % 1000;

  //Agregué la variable St para solucionar el problema de contar los minutos y horas.

  let St = Math.floor(((tiempo_ms - MS) / 1000));

  let S = St%60;
  let M = Math.floor((St / 60) % 60);
  let H = Math.floor((St/60 / 60));
  Number.prototype.ceros = function (n)
  {
    return (this + "").padStart(n, 0)
  }

  return H.ceros(2) + ":" + M.ceros(2) + ":" + S.ceros(2)  + "." + MS.ceros(3)
}


//ocultar todos los ejercicios menos el primero
function primero()
{

  // console.log("controles de inicio y fin de entrenos");

  var valores = document.getElementById('aejercicios').innerText;
  if( valores != null)
  {
    // console.log("si existe")
    // console.log(valores)

    array_valores = valores.split(',');

    for (var i=0; i<array_valores.length; i++)
    {
      var ejerc = "ejercicio";
      var btnFin = "fin";
      var divTiempos = "tiempos";


      ejerc+=i;
      btnFin+=i;
      divTiempos+=i;

      if(i == 0)
      {
        document.getElementById(ejerc).style.display = "block";
        document.getElementById(btnFin).style.display = "none";
        document.getElementById(divTiempos).style.display = "none";

        //console.log(array_valores[i].substr(1));

      }
      else if(i == (array_valores.length - 1))
      {
        document.getElementById(ejerc).style.display = "none";
        document.getElementById(divTiempos).style.display = "none";
        //console.log(array_valores[i].slice(0,-1));
      }
      else
      {
        document.getElementById(ejerc).style.display = "none";
        document.getElementById(divTiempos).style.display = "none";
        //console.log(array_valores[i]);
      }

      document.getElementById("aejercicios").style.display = "none";
      document.getElementById(divTiempos).style.display = "none";
    }

  }else
  {
    console.log("no existe")
  }

}


function comienza(id)
{
  console.log("funcion comienza");

  var valores = document.getElementById('aejercicios').innerText;


  if( valores != null)
  {
    // console.log("si existe")
    // console.log(valores)

    array_valores = valores.split(',');
    totalEjercicios = array_valores.length;

    if(parseInt(id) >= (totalEjercicios))
    {
      alert("ejercicio mayor");
    }else
    {
      if(parseInt(id) == 0)

      {
        var cAnterior = btnComienza+parseInt(id);
        var fAnterior = btnFin+parseInt(id);
        var divAnterior = divEjercicio+parseInt(id);
        var playanterior = btnPlay+(parseInt(id));
        var resetAnterior = btnReset+(parseInt(id));
        var pauseAnterior = btnPause+(parseInt(id));
        var divTiempoAnterior = divTiempos+(parseInt(id));
      }else
      {
        var cAnterior = btnComienza+(parseInt(id)-1);
        var fAnterior = btnFin+(parseInt(id)-1);
        var divAnterior = divEjercicio+(parseInt(id)-1);
        var playanterior = btnPlay+(parseInt(id)-1);
        var resetAnterior = btnReset+(parseInt(id)-1);
        var pauseAnterior = btnPause+(parseInt(id)-1);
        var divTiempoAnterior = divTiempos+(parseInt(id)-1);
      }

      var cActual = btnComienza+parseInt(id);
      var fActual = btnFin+parseInt(id);
      var divActual = divEjercicio+parseInt(id);
      var playActual = btnPlay+parseInt(id);
      var resetActual = btnReset+parseInt(id);
      var pauseActual = btnPause+parseInt(id);
      var divTiempoActual = divTiempos+(parseInt(id));


      var cSiguiente = btnComienza+(parseInt(id)+1);
      var fSiguiente = btnFin+(parseInt(id)+1);
      var divSiguiente = divEjercicio+(parseInt(id)+1);
      var playSiguiente = btnPlay+(parseInt(id)+1);
      var resetSiguiente = btnReset+(parseInt(id)+1);
      var pauseSiguiente = btnPause+(parseInt(id)+1);
      var divTiempoSiguiente = divTiempos+(parseInt(id)+1);




      //activar cronometro

      //activar fin

      // botones  comienza mostrar - fin ocultar
      document.getElementById(cActual).style.display = "none";
      document.getElementById(fActual).style.display = "block";
      document.getElementById(divTiempoActual).style.display = "block";
      
      reiniciar();
      cronometrar=true;
      console.log(playActual);
      console.log(pauseActual);
      console.log(resetActual);

      document.getElementById(playActual).style.display = "block";
      document.getElementById(pauseActual).style.display = "block";
      document.getElementById(resetActual).style.display = "block";

    }

  }else
  {
    console.log("no existen ejercicios")
  }

}

function fin(id)
{
  console.log("funcion fin");

  var valores = document.getElementById('aejercicios').innerText;

  if( valores != null)
  {
    // console.log("si existe")
    // console.log(valores)

    array_valores = valores.split(',');
    totalEjercicios = array_valores.length;
    
    if(parseInt(id) >= totalEjercicios)
    {
      alert("ejercicio mayor");
    }else
    {
      if(parseInt(id) == 0)

      {
        var cAnterior = btnComienza+parseInt(id);
        var fAnterior = btnFin+parseInt(id);
        var divAnterior = divEjercicio+parseInt(id);
      }else
      {
        var cAnterior = btnComienza+(parseInt(id)-1);
        var fAnterior = btnFin+(parseInt(id)-1);
        var divAnterior = divEjercicio+(parseInt(id)-1);
      }

      

      var cActual = btnComienza+parseInt(id);
      var fActual = btnFin+parseInt(id);
      var divActual = divEjercicio+parseInt(id);
      
      var cSiguiente = btnComienza+(parseInt(id)+1);
      var fSiguiente = btnFin+(parseInt(id)+1);
      var divSiguiente = divEjercicio+(parseInt(id)+1);
    


      if(parseInt(id) == (totalEjercicios-1))
      {
          //tiempo();    //pausar tiempo  //deterner y guardar valor

          //div
          document.getElementById(divActual).style.display = "none";
          //alert("FELICITACIONES TERMINASTE TU SESION DE HOY");
          totalDuracionEntreno+=acumulado;
          reiniciar();
          borrarlocal("id_plan");
          borrarlocal("id_sesion");
          //window.stop();
          window.location.href = "/workoutsapp/planes/";

      }else
      {
        //tiempo();    //pausar tiempo  //deterner y guardar valor

        //div
        document.getElementById(divActual).style.display = "none";
        document.getElementById(divSiguiente).style.display = "block";


        //boton
        document.getElementById(cSiguiente).style.display = "block";
        document.getElementById(fSiguiente).style.display = "none";
      }

      pausar();
      //console.log(formatearMS(acumulado));
      totalDuracionEntreno+=acumulado;
      //console.log(formatearMS(totalDuracionEntreno));

      reiniciar();
      
    }

  }else
  {
    console.log("no existen ejercicios")
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
      
      //comienza
      if(nombreclick.substr(0,8) == "comienza")
      {
        var id=nombreclick.substr(8);
        //console.log("comienza valor");
        //console.log(nombreclick.substr(8));
        comienza(id);

      }
      //fin
      if(nombreclick.substr(0,3) == "fin")
      {
        var id=nombreclick.substr(3);
        //console.log("fin valor");
        //console.log(nombreclick.substr(3));
        fin(id);
      }
      //play
      if(nombreclick.substr(0,4) == "play")
      {
        iniciar();
      }
      //play
      if(nombreclick.substr(0,5) == "pause")
      {
        pausar();
      }
      //play
      if(nombreclick.substr(0,5) == "reset")
      {
        reiniciar();
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


// blur Cuando el elemento pierde el foco.
// click El usuario hace clic sobre el elemento.
// dblclick El usuario hace doble clic sobre el elemento.
// focus El elemento gana el foco.
// keydown El usuario presiona una tecla.
// keypress El usuario presiona una tecla y la mantiene pulsada.
// keyup El usuario libera la tecla.
// load El documento termina su carga.
// mousedown El usuario presiona el botón del ratón en un elemento.
// mousemove El usuario mueve el puntero del ratón sobre un elemento.
// mouseout El usuario mueve el puntero fuera de un elemento.
// mouseover El usuario mantiene el puntero sobre un elemento.
// mouseup El usuario libera el botón pulsado del ratón sobre un elemento.
// unload El documento se descarga, bien porque se cierra la ventana, bien porque se navega a otra página.





//document.getElementById(comienza).addEventListener("click", tiempo);
//document.getElementById("fin0").addEventListener("click", mostrar);