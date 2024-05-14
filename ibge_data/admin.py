from django.contrib import admin
from ibge_data.models import UF, City


@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'UF')
