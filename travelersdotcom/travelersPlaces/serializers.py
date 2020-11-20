from rest_framework import serializers

from .models import *

from travelersReviewsComments.serializers import (
    TravelersVisitingPlaceReviewsCommentSerializers
)

class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'
        ordering = ['-id']

class AreasModelSerializer(serializers.ModelSerializer):
    # country=CountryModelSerializer(read_only=True)
    class Meta:
        model = AreasModel
        fields = '__all__'
        ordering = ['-id']


class ActivitiesAtPlacesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesAtPlacesModel
        fields = '__all__'
        ordering = ['-id']  


class PlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = '__all__'
        ordering = ['-id']  

class TravelersVisitingPlacesSerializer(serializers.HyperlinkedModelSerializer):
    #local_area=AreasModelSerializer(read_only=True)
    #category=PlaceCategorySerializer(many=True,read_only=True)
    #activites=ActivitiesAtPlacesModelSerializer(many=True,read_only=True)

    class Meta:
        model = TravelersVisitingPlaces
        fields = ['id','name','about','image','longitude','latitude','locality','categories','activities','reviews']
        ordering = ['-id']
