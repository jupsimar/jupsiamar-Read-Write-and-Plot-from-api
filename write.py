import urllib.request
import json
import time

for value in range(200):
    weather = f'http://api.openweathermap.org/data/2.5/weather?q=new+york&kathmandu&appid=65ad96e90e401baf71ab393dfffbc44d'

    response = urllib.request.urlopen(weather)
    weather_result = json.loads(response.read())

    temp_c = round(weather_result["main"]["temp"]-273.15,2)

    file1 = open("weather.txt","a")
    file1.write(f"{temp_c} \n")
    file1.close()

    print(value+1)
    time.sleep(0.25)