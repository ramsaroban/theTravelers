from django.contrib.gis import admin
from django.contrib.gis.geos import GEOSGeometry

from .models import TravelersLocation, TravelersVisitingPlaces

# Register your models here.

class TravelersLocationAdmin(admin.OSMGeoAdmin):
    list_display = ['label','latitude','longitude']
    search_field = ['label']

class TravelersVisitingPlacesAdmin(admin.OSMGeoAdmin):
    list_display = ['title','location','place_type']
    search_field = ['title','location','place_type']

admin.site.register(TravelersLocation,TravelersLocationAdmin)
admin.site.register(TravelersVisitingPlaces,TravelersVisitingPlacesAdmin)
