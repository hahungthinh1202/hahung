

output_object = document.getElementById("output");
number_array = [];
while (true){
  let input_number  = parseInt(prompt("Please enter a number(0 to exit): "))
  if (input_number === 0){
    break;
  }
  number_array.push(input_number)
}
number_array.sort(function(a, b){return b-a});
output_object.innerHTML = "Array of sorted array of number:<ol>";

for (let i = 0; i < number_array.length; i++)
  output_object.innerHTML += "<li>" + number_array[i] + "</li>";
output_object.innerHTML += "</ol>";

console.log(output_object.innerHTML)