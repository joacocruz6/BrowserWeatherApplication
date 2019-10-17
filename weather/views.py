import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    cities = City.objects.all()
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial?&appid=e010758d5c27c27970314c9a74fa6d04'
    weather_data = list()
    for city in cities:
        response = requests.get(api_url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = { 
        'weather_data' : weather_data,
        'form' : form,
         }
    return render(request,'weather/weather.html',context)