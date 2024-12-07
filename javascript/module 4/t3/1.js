searchValue = document.getElementById("query")
submitButton = document.getElementById("submit")
results = document.getElementById("results")
results.innerHTML = ""

submitButton.addEventListener('click', async function(event){
  event.preventDefault()
  let data_obj = await fetch(`https://api.tvmaze.com/search/shows?q=${searchValue.value}`)
  let data = await data_obj.json()
  data.forEach((item)=>{
    let article = document.createElement("article")
    let name  = document.createElement("h2")
    name.innerText = item.show.name
    let link = document.createElement("a")
    link.innerText = item.show.url
    link.target = "_blank"
    let newline = document.createElement("br")
    let image = document.createElement("img")
    image.src = item.show.image?.medium
    image.alt = "something"
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
