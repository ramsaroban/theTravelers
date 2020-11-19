from rest_framework import serializers

from .models import (
    TouristUserProfile,
    GuideUserProfile,
    TravelAgencyProfile,
)
from django.contrib.auth import get_user_model
Users = get_user_model()
from rest_framework.fields import CurrentUserDefault

class TouristProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = TouristUserProfile
        fields = '__all__'


    def create(self, validated_data):
        user= self.context['request'].user
        user = Users.objects.get(id=user.id)
        if user.user_type not in ['Tourist','TOURIST']:
          raise serializers.ValidationError({'error':'Inavlid user-type'})
        try:
            validated_data['user'] = user
            profile  = TouristUserProfile.objects.get(user=user)
            if profile:
                raise serializers.ValidationError({'error':'Profile already exist'}) 

            user_profile = TouristUserProfile(**validated_data)
        
            user_profile.save()
            return user_profile
        except Exception as e:
            raise e

class GuideUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model =  GuideUserProfile
        fields = '__all__'

    def create(self, validated_data):
        user= self.context['request'].user
        user = Users.objects.get(id=user.id)
        if user.user_type not in ['Guide','GUIDE']:
          raise serializers.ValidationError({'error':'Inavlid user-type'})
        try:
            validated_data['user'] = user
            profile  = GuideUserProfile.objects.get(user=user)
            if profile:
                raise serializers.ValidationError({'error':'Profile already exist'}) 

            user_profile = GuideUserProfile(**validated_data)
        
            user_profile.save()
            return user_profile
        except Exception as e:
            raise e


class TravelAgencyUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model =  TravelAgencyProfile
        fields = '__all__'
    
    def create(self, validated_data):
        user= self.context['request'].user
        user = Users.objects.get(id=user.id)
        if user.user_type not in ['Travel Agency', 'TRAVEL AGENCY']:
          raise serializers.ValidationError({'error':'Inavlid user-type'})
        try:
            validated_data['user'] = user
            profile  = TravelAgencyProfile.objects.get(user=user)
            if profile:
                raise serializers.ValidationError({'error':'Profile already exist'}) 

            user_profile = TravelAgencyProfile(**validated_data)
        
            user_profile.save()
            return user_profile
        except Exception as e:
            raise e