output_object = document.getElementById("output");
number_array = [];
while (true){
  let input_number  = parseInt(prompt("Please enter a number"))
  if (number_array.includes(input_number)){
    alert("That number has already been given!")
    break;
  }
  number_array.push(input_number)
}

output_object.innerHTML = "List of given numbers:<ul>";
for (let i = 0; i < number_array.length; i++)
  output_object.innerHTML += "<li>" + number_array[i] + "</li>";
output_object.innerHTML += "</ul>";

console.log(output_object.innerHTML)