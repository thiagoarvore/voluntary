from django.contrib import admin
from .models import Calendar


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('id', 'therapist', 'week_day','schedule', 'is_active')