

function Numeros(string) {//Solo numeros
    var out = '';
    var filtro = '1234567890';//Caracteres validos

for (var i=0; i<string.length; i++)
    if (filtro.indexOf(string.charAt(i)) != -1) 
        //Se añaden a la salida los caracteres validos
        out += string.charAt(i);

//Retornar valor filtrado
return out;
}

//solo letras
function letras(string){



    var out = '';
    var filtro = 'abcdefghijklmnñopqrstuvwxyz';//Caracteres validos

for (var i=""; i<string.length; i++)
    if (filtro.indexOf(string.charAt(i)) != -1) 
        //Se añaden a la salida los caracteres validos
        out += string.charAt(i);

//Retornar valor filtrado
return out;




}
//validar email
function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
  }
  
  function validate() {
    var $result = $("#result");
    var email = $("#txtCorreo").val();
    $result.text("");
  
    if (validateEmail(email)) {
      $result.text(email + " is valid :)");
      $result.css("color", "green");
    } else {
      $result.text(email + " is not valid :(");
      $result.css("color", "red");
    }
    return false;
  }
  
  $("#validate").bind("click", validate);

  //rut c
  function formatCliente (cliente) {
    cliente.value = cliente.value
      .replace(/[^0-9]/g, '')
      .replace( /^(\d{1,2})(\d{3})(\d{3})(\w{1})$/, '$1.$2.$3-$4')
  }