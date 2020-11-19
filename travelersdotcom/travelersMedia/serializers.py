from rest_framework import serializers

from .models import PlaceImageModel
from django.contrib.auth import get_user_model
Users = get_user_model()
from rest_framework.fields import CurrentUserDefault

class ImageModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlaceImageModel
        fields = ['uploader','place','title','alt','image','status',]