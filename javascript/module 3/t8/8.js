function compute(){
  let num1 = parseInt(document.getElementById("num1").value);
  let num2 = parseInt(document.getElementById("num2").value);
  let select = document.getElementById("operation");
  let result = document.getElementById("result");

  if (select.value === "add")
    result.textContent = num1 + num2;
  else if (select.value === "sub")
    result.textContent = num1 - num2;
  else if (select.value === "multi")
    result.textContent = num1 * num2;
  else if (select.value === "div")
    result.textContent = num1 / num2;
}

let calculate = document.getElementById("start");
calculate.addEventListener("click",compute);