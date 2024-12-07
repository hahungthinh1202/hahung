searchValue = document.getElementById("query")
submitButton = document.getElementById("submit")
results = document.getElementById("results")
results.innerHTML = ""

submitButton.addEventListener('click', async function(event){
  event.preventDefault()
  let data_obj = await fetch(`https://api.tvmaze.com/search/shows?q=${searchValue.value}`)
  let data = await data_obj.json()
  console.log(data)
  data.forEach((item)=>{

    let article = document.createElement("article")
    let newline = document.createElement("br")

    let name  = document.createElement("h2")
    name.innerText = item.show.name
    let link = document.createElement("a")
    link.innerText = item.show.url
    link.target = "_blank"
    let image = document.createElement("img")
    if(item.show.image === null)
      image.src = "https://via.placeholder.com/210x295?text=Not%20Found"
    else
      image.src = item.show.image.medium
    image.alt = "something else"
    let summary = document.createElement("div")
    summary.innerHTML = item['show']['summary']
    article.appendChild(name)
    article.appendChild(image)
    article.appendChild(newline)
    article.appendChild(link)
    article.appendChild(summary)
    results.appendChild(article)
  })
})
