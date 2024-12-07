searchValue = document.getElementById("query")
submitButton = document.getElementById("submit")


submitButton.addEventListener('click', async function(event){
  event.preventDefault()
  let data_obj = await fetch(`https://api.tvmaze.com/search/shows?q=${submitButton.value}`)
  let data = await data_obj.json()
  console.log(data)
})
