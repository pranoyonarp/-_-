#COMMAND LINE WEATHER APP USING WEATHER API(OpenWeatherMapAPI) 
import requests, json
api_key = "e4b9b8de52a23e92687fc7d7c4504b60"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "q=" + city_name + "&APPID=" + api_key
response = requests.get(complete_url)
data=response.json()
#print(data)
print(data['weather'][0]['main'])
print(data['main']['humidity'])
print(data['main']['temp'])
