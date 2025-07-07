from django.contrib import admin
from .models import Visitor

# Register your models here.

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'page_visited', 'visited_at', 'user_agent_short')
    list_filter = ('visited_at', 'page_visited')
    search_fields = ('ip_address', 'user_agent')
    readonly_fields = ('ip_address', 'user_agent', 'visited_at', 'page_visited')
    ordering = ('-visited_at',)
    
    def user_agent_short(self, obj):
        if obj.user_agent:
            return obj.user_agent[:50] + '...' if len(obj.user_agent) > 50 else obj.user_agent
        return 'Не указан'
    user_agent_short.short_description = 'User Agent (кратко)'
    
    def has_add_permission(self, request):
        return False  # Запрещаем ручное добавление записей
