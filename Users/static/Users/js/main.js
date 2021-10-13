window.onload = function() {

  for (let index = 0; index <= 9; index++) {
    progreso = document.getElementById('progreso'+index.toString())
    valor = progreso.getAttribute('value')
    if(valor < 1.25 && valor >0){
      valor = 25
    }
    else if(valor < 2.5 && valor >1.25){
      valor = 50
    }
    else if(valor < 3.75 && valor >2.5){
      valor = 75
      
    }else{

      valor = 100
    }
    progreso.setAttribute('class', 'progress-bar w-'+valor)
    progreso.setAttribute('aria-valuenow', valor)
    
  }

};