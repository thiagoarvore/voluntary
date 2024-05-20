import requests
from django.core.management.base import BaseCommand
from ibge_data.models import UF, City


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        states_raw = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        data = states_raw.json()
        for state in data:
            name = state['nome']
            if not UF.objects.filter(name=name):
                UF.objects.get_or_create(name=name)
        cities_raw = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/municipios')
        city_data = cities_raw.json()
        for city in city_data:
            name = city['nome']
            uf_raw = city['regiao-imediata']['regiao-intermediaria']['UF']['nome']
            uf = UF.objects.get(name=uf_raw)
            City.objects.get_or_create(name=name, UF=uf)
