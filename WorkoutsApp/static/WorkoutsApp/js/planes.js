//alert("planes mi papa");

//globals
var local = localStorage;
var id_plan="";
var id_sesion="";
var estadoPlan = false;
var estadoSesion = false;

window.onload = function()
{
    //mostrar();

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




function una()
{
    //location.href = "/workoutsapp/dashboard/";
    var myRedirect = function(redirectUrl, arg, value) {
        var form = $('<form action="' + redirectUrl + '" method="post">' +
        '<input type="hidden" name="'+ arg +'" value="' + value + '"></input>' + '</form>');
        $('body').append(form);
        $(form).submit();
      };

      myRedirect("/workoutsapp/dashboard/", "codigoplan", "1");
}

function dos()
{
    var var_1 = '1';
    //location.href = "/workoutsapp/dashboard/";
    $(function() {

        $('#btn_save').on('click', function() {
  
            $.post('/workoutsapp/dashboard/', {
                "codigoplan": var_1//, "var_2": var_2, "var_3": var_3, "var_4": var_4
              },function(data) {
                console.log('procesamiento finalizado', data);
            });
        })
  
  })
}

function redirecciona()
{
    var select = document.getElementById('codigoplan');
    select.addEventListener('change',
    function()
    {
        var selectedOption = this.options[select.selectedIndex];
        console.log(selectedOption.value + ': ' + selectedOption.text);
    });
}



//saber que evento sucede y capturarlo
function conocerEvento(e)
{

	var evento = e || window.event;

		//document.getElementById("evento").value = e.type;

    // console.log("evento");
    // console.log(e);

    if(evento.type == "click")
    {

        //console.log("nombre del click");
        //console.log(evento.path[0].id);

        var nombreclick=evento.path[0].id;


        //continuar
        if(nombreclick.substr(0,10) == "continuar")
        {
            //alert("click");
            //var id=nombreclick.substr(7);
            //console.log("comienza valor");
            //console.log(nombreclick.substr(8));
            //alert("empezo entreno");

            //id_plan = document.getElementById("codigoplan").value;
            //console.log(id_sesion);
            //almacenarlocal('id_plan', id_plan);
            //una();

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