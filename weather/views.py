from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import Visitor
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


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

def visitor_stats(request):
    """Страница со статистикой посетителей"""
    # Получаем общую статистику
    total_visitors = Visitor.objects.count()
    
    # Посетители за последние 24 часа
    yesterday = timezone.now() - timedelta(days=1)
    visitors_today = Visitor.objects.filter(visited_at__gte=yesterday).count()
    
    # Посетители за последние 7 дней
    week_ago = timezone.now() - timedelta(days=7)
    visitors_week = Visitor.objects.filter(visited_at__gte=week_ago).count()
    
    # Уникальные IP адреса
    unique_ips = Visitor.objects.values('ip_address').distinct().count()
    
    # Последние 20 посетителей
    recent_visitors = Visitor.objects.all()[:20]
    
    # Топ страниц по посещениям
    top_pages = Visitor.objects.values('page_visited').annotate(
        count=Count('page_visited')
    ).order_by('-count')[:10]
    
    context = {
        'total_visitors': total_visitors,
        'visitors_today': visitors_today,
        'visitors_week': visitors_week,
        'unique_ips': unique_ips,
        'recent_visitors': recent_visitors,
        'top_pages': top_pages,
    }
    
    return render(request, 'weather/visitor_stats.html', context)
