function mouseIn(){
  let target = document.getElementById("target")
  target.src = "img/picB.jpg"
}

function mouseOut(){
  let target = document.getElementById("target")
  target.src = "img/picA.jpg"
}
let trigger = document.getElementById("trigger")
trigger.addEventListener("mouseenter",mouseIn)
trigger.addEventListener("mouseout",mouseOut)
