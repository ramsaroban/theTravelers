from rest_framework import serializers

from .models import *



class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'

class AreasModelSerializer(serializers.ModelSerializer):
    # country=CountryModelSerializer(read_only=True)
    class Meta:
        model = AreasModel
        fields = '__all__'


class ActivitiesAtPlacesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesAtPlacesModel
        fields = '__all__'   


class PlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = '__all__'  

class TravelersVisitingPlacesSerializer(serializers.ModelSerializer):
    local_area=AreasModelSerializer(read_only=True)
    category=PlaceCategorySerializer(many=True,read_only=True)
    activites=ActivitiesAtPlacesModelSerializer(many=True,read_only=True)

    class Meta:
        model = TravelersVisitingPlaces
        fields = '__all__' 
    