from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from locationapp.models import Place
import csv


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open("./places_list.csv", mode="r") as file:
            places_file = csv.DictReader(file)
            for place in places_file:
                co_ordinates = Point(
                    float(place.get("Longitude")), float(place.get("Latitude"))
                )
                place_instance = Place.objects.create(
                    name=place.get("City Name"),
                    description=place.get("Description"),
                    location=co_ordinates,
                )
                print(f"{place_instance.name} succesfully added to the databse.")
