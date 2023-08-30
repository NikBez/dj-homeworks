import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:

            Phone.objects.create(name=phone.get('name'),
                                 image=phone.get('image'),
                                 price=phone.get('price'),
                                 release_date=datetime.strptime(phone.get('release_date'), '%Y-%m-%d'),
                                 lte_exists=True if phone.get('lte_exists') == 'True' else False,
                                 )
        print('Loading complite')
