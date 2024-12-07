submitButton = document.getElementById("button")
target = document.getElementById("target")
submitButton.addEventListener('click', async function(event){
  event.preventDefault()
  let data_obj = await fetch(`https://api.chucknorris.io/jokes/random`)
  let data = await data_obj.json()
  let joke = document.createElement("p")
  joke.innerHTML = data.value
  target.appendChild(joke)
})
