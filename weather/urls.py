from django.urls import path
from .views import get_weather, index

urlpatterns = [
    path('', index, name='index'),
    path('api/', get_weather, name='get_weather'),
] 