from django.shortcuts import render
import requests
from . models import weatherDb

# Create your views here.
def index(request):

    #city = 'London'
    city_weather = {}

    if request.method == 'POST':

        city = request.POST.get('cityname')
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=92eabd7e33187ac9ec4d563de8489cfe&units=metric"


        '''
        requests is a popular third-party Python library used to send HTTP requests (like GET, POST, etc.) easily.

        It's not part of Django — it's a general-purpose Python package used to interact with web APIs (like OpenWeatherMap).

        requests.get(...) is used to send an HTTP GET request to a given URL and retrieve data from it.

        '''
        data = requests.get(url.format(city)).json()
        # print(data)
        
        if data.get("cod") == 200:
            city_weather = {
                'city' : data['name'],
                'temperature' : data['main']['temp'],
                'description' : data['weather'][0]['description'],
                'pressure' : data['main']['pressure'],
                'humidity' : data['main']['humidity'],
                'icon' : data['weather'][0]['icon']
            }

            obj = weatherDb(city=city, temperature=city_weather['temperature'], 
                            description=city_weather['description'],
                            pressure = city_weather['pressure'],
                            humidity = city_weather['humidity'])
            obj.save()

        else:
            city_weather = {"Error":"City weather is not available"}

        # print(city_weather)

    return render(request, 'weather.html', {'weather':city_weather})