function getCookie(name){
    if(document.cookie.length == 0)
      return null;

    var regSepCookie = new RegExp('(; )', 'g');
    var cookies = document.cookie.split(regSepCookie);

    for(var i = 0; i < cookies.length; i++){
      var regInfo = new RegExp('=', 'g');
      var infos = cookies[i].split(regInfo);
      if(infos[0] == name){
        return unescape(infos[1]);
      }
    }
    return null;
  }

var First_Name = getCookie('First_Name')
var Name = getCookie('Name')
if(First_Name == null)
window.onload = function(){
    window.location.href = "Home.html";
    }
document.getElementById("H2").innerHTML = ('<b>Hello</b> ' + First_Name + " " + Name + ' <b>!</b>');
