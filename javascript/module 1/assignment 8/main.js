
function check_leap_year(year){
  year  = parseInt(year)
  return (year%4 == 0) && (year%400 != 0);
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
output_object.innerHTML = output;