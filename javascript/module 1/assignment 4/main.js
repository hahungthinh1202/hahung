let name  = prompt("please enter your name");
let house = ""
random_number = Math.floor(Math.random()*4);

switch (random_number){
    case 0:
      house = "Gryffindor"
      break;
    case 1:
      house = "Slytherin"
      break;
    case 2:
      house = "Hufflepuff"
      break;
    case 3: house = "Ravenclaw"
      break;
}

console.log(house)

document.getElementById("output").innerHTML = name + ", you are " + house + "."