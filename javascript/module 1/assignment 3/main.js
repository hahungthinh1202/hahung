var num1, num2, num3;

num1 = parseInt(prompt("please enter the 1st number"))
num2 = parseInt(prompt("please enter the 2nd number"))
num3 = parseInt(prompt("please enter the 3rd number"))
output_text =
    "Three number: " + num1 + ", " + num2 + ", " + num3 + "<br>" +
    "Sum: " + (num1+num2+num3) + "<br>" +
    "Product: " + (num1*num2*num3) + "<br>" +
    "Average: " + (num1+num2+num3)/3 + "<br>"

output_object = document.getElementById("output")
output_object.innerHTML = output_text
