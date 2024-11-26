

function even(input_array){
  let output_array = [];
  for (let i = 0; i < input_array.length; i++){
    if (input_array[i] % 2 === 0){
      output_array.push(input_array[i])
    }
  }
  return output_array;
}


original_array = [2,5,7,8,9,10]
console.log(even(original_array))