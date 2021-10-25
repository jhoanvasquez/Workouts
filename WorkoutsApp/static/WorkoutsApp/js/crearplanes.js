
window.onload = function()
{
    //alert("validando su plan a crear");
    document.getElementById("acantidadEjercicios").style.display = "none";
    document.getElementById('btnCrearPlan').disabled=true;
    document.getElementsByName('id_area')[0].addEventListener('change', validaEjercicios);
};


function validaEjercicios()
{
    // alert("validando ejercicios de este plan");
    
    var valores = document.getElementById('acantidadEjercicios').innerText;
    document.getElementById("acantidadEjercicios").style.display = "none";
   
    array_valores = valores.split(',');
    
    //capturar selec y validar que laposicion que selecciono sea mayor a 8
    var cod = document.getElementsByName('id_area')[0].value;
    var cod1=cod-1;
    var cantEjercicios=0;


    if(cod1 >= 0 )
    {
        //validar que sea el primero
        if(cod1 == 0)
        {
            cantEjercicios = array_valores[0].split('[')[1];
        }

        //mitad
        if(cod1 > 0  && cod1 < array_valores.length-1)
        {
            cantEjercicios = array_valores[cod1];
            //alert('mitad ' + cod1 + ' ' + array_valores[cod1]);
        }
        //validar que sea el ultimo
        if(cod1 == array_valores.length-1)
        {
            cantEjercicios = array_valores[cod1].substr(0, (array_valores[cod1].length-1));
            //alert('ultimo ' + cod1 + ' ' + array_valores[cod1].substr(0, (array_valores[cod1].length-1)));
        }
    }

    if(parseInt(cantEjercicios) > 8)
    {
        //alert('Habilitar boton para Crear plan');
        document.getElementById('btnCrearPlan').disabled=false;
    }else{
        if(cod1 >= 0)
        {
            alert('Por favor selecciona otro plan, ya que este aun no cuenta con suficientes ejercicios.');
            document.getElementById('btnCrearPlan').disabled=true;
        }
        document.getElementById('btnCrearPlan').disabled=true;
    }
}
