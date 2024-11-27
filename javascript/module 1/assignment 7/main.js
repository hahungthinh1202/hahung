function dice_roll(){
  return Math.floor(Math.random()*6+1)
}

let roll_time = parseInt(prompt("How many times you want to roll your dice: "))
let sum = 0;
for (let i = 0; i < roll_time; i++ )
  sum += dice_roll();

let output_object = document.getElementById("output")
output_object.innerHTML = "The sum of " + roll_time + " dice rolls is " + sum
