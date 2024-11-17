const answer = confirm('Should I calculate the square root?');

output_object = document.getElementById("output")
if (answer){
  number = parseInt(prompt("Please enter a number "))
  s = number**(1/2)
  output_object.innerHTML = "Square root of " + number + " is " + number**(1/2)
}
else{
  output_object.innerHTML = "The square root is not calculated."
}



