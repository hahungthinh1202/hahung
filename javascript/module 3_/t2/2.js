let target = document.getElementById("target")
first = document.createElement("li")
first.innerHTML = "First item"
second  = document.createElement("li")
second.innerHTML = "Second item"
third = document.createElement("li")
third.innerHTML = "Third item"
target.appendChild(first)
target.appendChild(second)
target.appendChild(third)
target.classList.add("my-item")