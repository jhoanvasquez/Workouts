//alert("todo se ejecuta mi papusito")
window.onload = function() {
  //hola();
  validarFechas();
  //document.getElementById('card0').innerHTML += "28-08-2021"
};

function hola()
{
  //alert("todas las sesiones aqui social12")
  console.log('hola')
  //array.forEach(element => {   });

}

function validarFechas()
{

  for (let step = 0; step < 5; step++) 
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
/* document.write(d.getDate()); */
/* document.write(d.getMonth()); */
/* document.write(d.getDay()); */
/* document.write(d.getYear()+1900); */



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