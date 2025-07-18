# Generated by Django 4.2.13 on 2025-07-07 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('user_agent', models.TextField(blank=True, null=True, verbose_name='User Agent')),
                ('visited_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время посещения')),
                ('page_visited', models.CharField(blank=True, max_length=255, null=True, verbose_name='Посещенная страница')),
            ],
            options={
                'verbose_name': 'Посетитель',
                'verbose_name_plural': 'Посетители',
                'ordering': ['-visited_at'],
            },
        ),
    ]
