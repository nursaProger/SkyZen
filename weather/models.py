from django.db import models
from django.utils import timezone

# Create your models here.

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="IP адрес")
    user_agent = models.TextField(blank=True, null=True, verbose_name="User Agent")
    visited_at = models.DateTimeField(default=timezone.now, verbose_name="Время посещения")
    page_visited = models.CharField(max_length=255, blank=True, null=True, verbose_name="Посещенная страница")
    
    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
        ordering = ['-visited_at']
    
    def __str__(self):
        return f"{self.ip_address} - {self.visited_at}"
