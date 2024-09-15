from django.contrib import admin
from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'therapist', 'patient', 'schedule', 'is_active')
    search_fields = ('therapist__name', 'patient__name',)
