import requests
from django.shortcuts import render
from .models import City
# Create your views here.
def index(request):
    cities = City.object.all()
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial?&appid=e010758d5c27c27970314c9a74fa6d04'
    weather_data = list()
    for city in cities:
        response = request.get(api_url.format(city))
        city_weather = {
        'city': city,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = { 
        'weather_data' : weather_data,
         }
    return render(request,'weather/weather.html',context)