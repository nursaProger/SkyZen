from django.urls import path
from .views import get_weather, index, visitor_stats

urlpatterns = [
    path('', index, name='index'),
    path('api/', get_weather, name='get_weather'),
    path('stats/', visitor_stats, name='visitor_stats'),
] 