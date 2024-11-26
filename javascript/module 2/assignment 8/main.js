

function concat(input_array){
  let output = "";
  for (let i = 0; i < input_array.length; i++){
    output += input_array[i];
  }
  return output;
}

original_array = ["Johnny", "DeeDee", "Joey", "Marky"]
test_element = document.getElementById("output");
test_element.innerHTML = ("orginal array: [\"Johnny\", \"DeeDee\", \"Joey\", \"Marky\"] <br> function output: " + concat(original_array))
