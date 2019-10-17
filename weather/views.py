import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    city = 'Región Metropolitana de Santiago'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial?&appid=e010758d5c27c27970314c9a74fa6d04'
    response = requests.get(api_url).json()
    print(response)
    city_weather = {
        'city': city,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon'],
    }
    
    context = { 'city_weather' : city_weather }
    return render(request,'weather/weather.html',context)