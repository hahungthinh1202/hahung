function dice(max){
  return Math.floor(Math.random()*max+1);
}

let max_roll = parseInt(prompt("Enter the maximum value of your dice:"));
let roll_result = 0;
while(true){
  roll_result = dice(max_roll);
  console.log(roll_result)
  if (roll_result === max_roll){
    break;
  }
}