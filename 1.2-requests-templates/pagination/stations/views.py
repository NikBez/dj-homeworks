from csv import DictReader

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    file_path = settings.BUS_STATION_CSV
    bus_stations = []

    with open(file_path, encoding='utf-8', newline='') as from_csv:
        reader = DictReader(from_csv, delimiter=';')
        for station in reader:
            bus_stations.append({
                'Name': station.get('Name', 'Empty'),
                'Street': station.get('PlaceDescription', 'Empty'),
                'District': station.get('District', 'Empty'),
            })

    paginator = Paginator(bus_stations, 10)
    current_page = request.GET.get('page', 1)

    context = {
        'bus_stations': paginator.page(current_page).object_list,
        'page': paginator.page(current_page),
    }
    return render(request, 'stations/index.html', context)
