tds = document.querySelectorAll("td")
restart = document.querySelector("#restart")

for(var i=0;i<tds.length;i++){
  tds[i].addEventListener("click",function(){
    if(this.textContent === '0')
      this.textContent = ''    // use this if multiple contents sets a same objects
    else if(this.textContent === 'X')
      this.textContent = '0'
    else
      this.textContent = 'X'
  })
}

//document.querySelectorAll("#one")


restart.addEventListener("click",function(){
    for(var i=0;i<tds.length;i++){
      tds[i].textContent = ''
    }

})
