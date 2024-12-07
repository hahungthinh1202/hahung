submitButton = document.getElementById("button")
submitButton.addEventListener('click', async function(event){
  event.preventDefault()
  let data_obj = await fetch(`https://api.chucknorris.io/jokes/random`)
  let data = await data_obj.json()
  console.log(data.value)
})
