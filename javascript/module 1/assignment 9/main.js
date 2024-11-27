
function check_prime(number){
    let upper_limit = Math.ceil(number ** 0.5);
    let output = "";
    if(number === 1 || number === 2)
        output = "prime!";
    else {
        for (let i = 2; i < (upper_limit + 1); i++) {
            if (number % i === 0){
                output = "not prime!";
                break;
            }
            else if (i === upper_limit)
                output = "prime!";
        }
    }
    return output
}

let output_object = document.getElementById("output")
let InputNumber = parseInt(prompt("Please enter your number: "))
output_object.innerHTML = check_prime(InputNumber);