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

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var First_Name = getCookie('First_Name')
var Name = getCookie('Name')
if(First_Name == null){
Swal.fire({
  title: 'You has been deconnected !',
  icon: 'warning',
  showConfirmButton: false,
  timer: 2000,
  timerProgressBar: true,
})
await sleep(2000)
window.onload = function(){
  window.location.href = "Bin/Site/Html/Home.html";
}
}