function compute() {
  let calculation = document.getElementById("calculation").value
  let result = document.getElementById("result")
  let num  = []
  if (calculation.includes("+")){
    num = calculation.split("+")
    result.innerText = parseInt(num[0]) + parseInt(num[1])
  }
  else if (calculation.includes("-")){
    num = calculation.split("-")
    result.innerText = parseInt(num[0]) - parseInt(num[1])
  }
  else if (calculation.includes("*")){
    num = calculation.split("*")
    result.innerText = parseInt(num[0]) * parseInt(num[1])
  }
  else if (calculation.includes("/")){
    num = calculation.split("/")
    result.innerText = parseInt(num[0]) / parseInt(num[1])
  }
}

let calculate = document.getElementById("start");
calculate.addEventListener("click",compute);