var mouseOver = document.querySelector("#mouseOver")
var click = document.querySelector("#click")
var doubleClick = document.querySelector("doubleClick")

mouseOver.addEventListener("mouseover",function(){
  mouseOver.textContent = "Mouse over"
  mouseOver.style.color = "red"
})

mouseOver.addEventListener("mouseout",function(){
  mouseOver.textContent = "Mouse Out"
  mouseOver.style.color = "black"
})

click.addEventListener("click",function(){
  click.textContent = "Clicked:)"
  click.style.color = "blue"
})

doubleClick.addEventListener("doubleclick",function(){
  doubleClick.textContent = "Double Clicked:)"
  doubleClick.style.color = "green"
})
