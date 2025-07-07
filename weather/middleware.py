from django.utils.deprecation import MiddlewareMixin
from .models import Visitor
from django.utils import timezone

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Получаем IP адрес посетителя
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # Получаем User Agent
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Получаем текущий путь
        page_visited = request.path
        
        # Сохраняем информацию о посетителе
        try:
            Visitor.objects.create(
                ip_address=ip,
                user_agent=user_agent,
                page_visited=page_visited,
                visited_at=timezone.now()
            )
        except Exception as e:
            # Логируем ошибку, но не прерываем запрос
            print(f"Ошибка при сохранении посетителя: {e}")
        
        return None 