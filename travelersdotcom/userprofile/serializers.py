from rest_framework import serializers
from .models import TouristUserProfile,GuideUserProfile,TravelAgencyProfile

class TouristUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model =  TouristUserProfile
        fields = '__all__'

class GuideUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model =  GuideUserProfile
        fields = '__all__'


class TravelAgencyUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model =  TravelAgencyProfile
        fields = '__all__'