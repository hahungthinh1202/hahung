import requests
data = requests.get("https://api.chucknorris.io/jokes/random")
print(data.json()['value'])