

output_object = document.getElementById("output");
participant_array = [];
participant_number = parseInt(prompt("Please enter the number of participant: "));
console.log(participant_number)
for (let i = 0; i < participant_number; i++)
  participant_array[i] = prompt("Please enter the name of the " + (i+1) + " person");

output_object.innerHTML = "Participants list in alphabetical order:<ol>";
participant_array.sort();
for (let i = 0; i < participant_number; i++)
  output_object.innerHTML += "<li>" + participant_array[i] + "</li>";
output_object.innerHTML += "</ol>";

console.log(output_object.innerHTML)