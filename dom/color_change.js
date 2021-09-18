var myHeader = document.querySelector("h1");

function getRandomColor(){

  var i = Math.floor(Math.random()*4)
  var colors = ["#ff0000","#ffff00","#0000ff","#00ff00"];
  return colors[i];
}

function setColor(){
  myHeader.style.color = getRandomColor();
}

setInterval("setColor()",1000);
