from django.shortcuts import render, redirect
from .models import FavoriteCity
import requests
from django.conf import settings

# Fetch weather data from the OpenWeatherMap API
def fetch_weather(city):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Home view to display weather and favorite cities
def home(request):
    if request.user.is_authenticated:
        favorites = FavoriteCity.objects.filter(user=request.user)
        weather_data = [fetch_weather(city.city_name) for city in favorites]
    else:
        weather_data = []
    return render(request, 'home.html', {'weather_data': weather_data})

# Add a favorite city
def add_favorite(request):
    if request.method == 'POST' and request.user.is_authenticated:
        city_name = request.POST.get('city_name')
        if city_name:
            FavoriteCity.objects.get_or_create(user=request.user, city_name=city_name)
        return redirect('home')
    return redirect('home')

# Remove a favorite city
def remove_favorite(request, city_id):
    if request.user.is_authenticated:
        FavoriteCity.objects.filter(id=city_id, user=request.user).delete()
    return redirect('home')
