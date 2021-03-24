$(function(){
    
    $('#btn').on('click', function () {
      
  
      $.ajax({
        url: "http://localhost:8000/prueba1",
        type:"POST",
        
        data: {
          'username': "username"
        },
        dataType: 'json',

        success:function(response){
         alert("response")
  
        },
        error: function (errors) {
            alert(errors)
        }
  
      });
      
  
    });
  
   
  });
  