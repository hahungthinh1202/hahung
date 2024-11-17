
function dice_roll(){
  return Math.floor(Math.random()*6+1)
}
output_object = document.getElementById("output")

roll_time = parseInt(prompt("How many times you want to roll your dice: "))

var sum = 0;
for (let i = 0; i < roll_time; i++ ){
  sum += dice_roll();

}

output_object.innerHTML = "The sum of " + roll_time + " dice roll is " + sum
