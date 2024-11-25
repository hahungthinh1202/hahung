


//declaring some variables
output_object = document.getElementById("output");
candidates_array = [];
winner = 0;
winner_votes= 0;

candidates_number = parseInt(prompt("Please enter the number of candidates: "));
for (let i = 0; i < candidates_number; i++){
  candidates_array[i] = {}
  candidates_array[i].name = prompt("Name for candidate " + (i+1) + ": ");
  candidates_array[i].votes = 0;

}

voters_number = parseInt(prompt("Please enter the number of voters: "));


for (let voter = 0; voter < voters_number; voter++) {
  let voter_vote = prompt("Voter number " + (voter+1) + ": " );
  for (let candidate = 0 ;  candidate < candidates_number; candidate++){
    if (voter_vote === candidates_array[candidate].name){
      candidates_array[candidate].votes++;
      if (candidates_array[candidate].votes > winner_votes){
        winner = candidate
        winner_votes = candidates_array[candidate].votes
      }
    }
  }
}

output_object.innerHTML = "The winner is " + candidates_array[winner].name + " with " + candidates_array[winner].votes + " votes. <br> Results:<ol>"
for (let candidate = 0 ;  candidate < candidates_number; candidate++)
  output_object.innerHTML += "<li>" +  candidates_array[candidate].name + ": " + candidates_array[candidate].votes + " votes</li>"

output_object.innerHTML += "</ol>"
