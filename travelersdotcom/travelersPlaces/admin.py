from django.contrib.gis import admin
from django.contrib.gis.geos import GEOSGeometry

from .models import (
    TravelersUserLocation,
    TravelersVisitingPlaces,
    CountryModel,
    ActivitiesAtPlacesModel,
    AreasModel,
    PlaceCategory
)

# Register your models here.

class TravelersUserLocationAdmin(admin.OSMGeoAdmin):
    list_display = ['user','latitude','longitude']
    search_field = ['user']

class TravelersVisitingPlacesAdmin(admin.OSMGeoAdmin):
    list_display = ['id','name','latitude','longitude','image']
    search_field = ['name']

class CountryModelAdmin(admin.OSMGeoAdmin):
    list_display = ['name','image']
    serch_field  = ['name']

class AreasModelAdmin(admin.OSMGeoAdmin):
    list_display = ['country','name','latitude','longitude','image']
    search_field = ['country','name']

class PlaceCategoryAdmin(admin.OSMGeoAdmin):
    list_display = ['category','image']
    search_field = ['category']

class ActivitiesAtPlacesModelAdmin(admin.OSMGeoAdmin):
    list_display = ['id','name','image']
    search_filed = ['name']

admin.site.register(TravelersUserLocation, TravelersUserLocationAdmin)
admin.site.register(TravelersVisitingPlaces, TravelersVisitingPlacesAdmin)
admin.site.register(CountryModel, CountryModelAdmin)
admin.site.register(AreasModel, AreasModelAdmin)
admin.site.register(PlaceCategory, PlaceCategoryAdmin)
admin.site.register(ActivitiesAtPlacesModel, ActivitiesAtPlacesModelAdmin)