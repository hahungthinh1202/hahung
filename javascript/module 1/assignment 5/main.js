function check_leap_year(year){
  year  = parseInt(year)
  return (year%4 == 0) && (year%400 != 0);
}

let year = prompt("Please enter a year: ");
var str = "";
if (check_leap_year(year)){
  str = " is leap year.";
}
else
  str = " is not a leap year.";
document.getElementById("output").innerHTML = "Year " + year + str
