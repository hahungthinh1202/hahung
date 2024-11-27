let output_object = document.getElementById("output")
let output_array = []
for (let i = 0; i < 5; i++)
  output_array[i] = parseInt(prompt("Please enter the " + (i+1) + " number "))
output_object.innerHTML = "Input array in reverse order: "
for (let i = 4; i >= 0; i--)
  output_object.innerHTML = output_object.innerHTML + output_array[i] + " "