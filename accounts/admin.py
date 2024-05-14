from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'photo',
        'address',
        'name',
        'whatsapp',
        'crp',
        'crp_check',
        'platform',
        'trained',
        'age',
        'city',
        'uf',
        'emergency_number',
        'psychiatric',
        'complaint',
    )
