
function check_leap_year(year){
  return (year%4 === 0) && (year%400 !== 0);
}

let output_object = document.getElementById("output")
let start_year = parseInt(prompt("Please enter your start year: "))
let end_year = parseInt(prompt("Please enter your end year: "))
let output = ""
for( let i = start_year; i <= end_year; i++ ){
  if (check_leap_year(i)){
    output += "<li>" + i + "</li>"
  }
}
output_object.innerHTML = output;