
function check_prime(number){
  if (number <= 1 ){
    return false
  }

}

output_object = document.getElementById("output")
start_year = parseInt(prompt("Please enter your start year: "))
end_year = parseInt(prompt("Please enter your end year: "))
output = ""
for( let i = start_year; i <= end_year; i++ ){
  if (check_leap_year(i   )){
    output += "<li>" + i + "</li>"
  }
}
output_object.textContent = output;