function dice(){
  return Math.floor(Math.random()*6+1);
}


let roll_result = 0;
while(true){
  roll_result = dice();
  console.log(roll_result)
  if (roll_result === 6){
    break;
  }
}