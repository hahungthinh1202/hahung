function dice_roll(){
    return Math.floor(Math.random()*6+1)
}

let roll_times = parseInt(prompt("Enter the number of dice rolls: "));
let interest_number = parseInt(prompt("Enter your target sum of all dice roll: "));

const sample = 10000;
let temp_sum = 0;
let output = 0;
for (let i = 0; i < sample; i++){
    for (let j = 0; j < roll_times; j++){
        temp_sum += dice_roll();
    }
    if (temp_sum === interest_number)
        output++;
    temp_sum = 0;
}
output = output*100/sample;
output = output.toFixed(2) +"%";
let target = document.getElementById("output")
target.innerHTML = "Probability to get sum " + interest_number + " with " + roll_times + " dice is " + output