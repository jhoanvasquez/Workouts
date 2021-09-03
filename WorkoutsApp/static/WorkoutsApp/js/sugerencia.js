//Manejo de la info del form para registrar usuario
alert("Sugerencia");

let input1 = document.getElementById('campo1');

input1.addEventListener('keyup',(event)=>{
  let texto = event.target.value;
  console.log(texto)
  
  let texto_a_mostrar="";
  document.getElementById('campo3').value = texto;
})