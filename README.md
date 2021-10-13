# python scripts


## script to print weather/date in linux terminal: python-weather.py
A simple Python script for linux users, using Pyfiglet and openweatherapi that prints the date, time, temperature, and atmospheric pressure all in your terminal

- Usage
first install pyfiglet for printing the ascii banner with the command `pip install pyfiglet`

Make an account on https://openweathermap.org/api and genererate an api key using the free version of the current weather data api

edit python-weather.py and place your api key in the variable `api_key = ("Your api key")`, then edit the variable `city_name = ("your city")`

Finally place the following command in your .bashrc file `python3 /home/name/Desktop/Python-weather.py`

