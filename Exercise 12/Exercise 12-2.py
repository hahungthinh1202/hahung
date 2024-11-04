import requests

city_name = input("Please enter a place you want to know the weather: ")
# Get the location latitude and longitude
location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={my_api_key}")
# After request the location, it will return a list of possible place, I choose the first one in the list
# Then using that location data to make another request for the actual weather
weather = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={location.json()[0]['lat']}&lon={location.json()[0]['lon']}&appid={my_api_key}")

data = weather.json()

# Print out the data
print(f"The current weather at {location.json()[0]['name']} is {data['current']['weather'][0]['main']} with {data['current']['weather'][0]['description']}"
      f". The temperature is {data['current']['temp']-273:.2f} degrees Celsius with humidity of {data['current']['humidity']}%")
