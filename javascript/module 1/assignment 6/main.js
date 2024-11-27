const answer = confirm('Should I calculate the square root?');

let output_object = document.getElementById("output")
if (answer){
  let number = parseInt(prompt("Please enter a number "))
  output_object.innerHTML = "Square root of " + number + " is " + number**(1/2)
}
else
  output_object.innerHTML = "The square root is not calculated."




