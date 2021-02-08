from rest_framework import serializers

from .models import *

class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        ordering = ['-id']