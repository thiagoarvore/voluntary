from django.contrib import admin
from .models import Treatment

# Register your models here.
@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'therapist', 'patient', 'schedule', 'is_active')
