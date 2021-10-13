import pyfiglet
from datetime import datetime
import requests, json

# PyFiglet for ascci banner and date/time
ascii_banner = pyfiglet.figlet_format("Your name")
print(ascii_banner)
print("Date: " + str(datetime.now()))

# pulling from weather api
api_key = "your api key"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = ("Your city")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]

    current_humidity = y["humidity"]

    current_pressure = y["pressure"]

    z = x["weather"]

    print("Temperature kelvin: " + str(current_temperature))
    print("Pressure hPa: " + str(current_pressure))
    print("Humidity percentage: " + str(current_humidity))
    
    # note: The indentation is like this because of the way it's interpreted by .bashrc it kept throwing unexpected indent errors using normal indenting

