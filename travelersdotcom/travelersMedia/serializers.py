from rest_framework import serializers

from .models import ImageModel
from django.contrib.auth import get_user_model
Users = get_user_model()
from rest_framework.fields import CurrentUserDefault

class ImageModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = ImageModel
        fields = ['user','title','alt','image','slug','status',]


 

