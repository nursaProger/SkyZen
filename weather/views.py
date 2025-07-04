from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'weather/index.html')

def get_weather(request):
    city = request.GET.get('city')
    api_key = getattr(settings, 'OPENWEATHERMAP_API_KEY', 'нет ключа')
    print('API KEY:', api_key)  # Для отладки
    if not city:
        return JsonResponse({'error': 'City parameter is required.'}, status=400)

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return JsonResponse({
                'error': data.get('message', 'Error fetching weather'),
                'raw': data,
                'city': city,
                'api_key': api_key
            }, status=400)
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return JsonResponse(weather)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
