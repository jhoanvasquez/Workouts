window.onload = function() {

  for (let index = 0; index <= 9; index++) {
    progreso = document.getElementById('progreso'+index.toString())
    valor = parseInt(progreso.getAttribute('value'))
    console.log(valor);
    if(valor <= 25 && valor >= 0){
      valor = 25
    }
    else if(valor <= 50 && valor > 25){
      valor = 50
    }
    else if(valor <= 70 && valor > 50){
      valor = 75
    }
    else{
      valor = 100
    }
    
    
    progreso.setAttribute('class', 'progress-bar w-'+valor)
    progreso.setAttribute('aria-valuenow', valor)
    valor = 0
    
  }

};