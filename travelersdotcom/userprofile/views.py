from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *

class TouristUserProfileViewset(viewsets.ModelViewSet):
    queryset = TouristUserProfile.objects.all()
    serializer_class = TouristUserProfileSerializers
    
class GuideUserProfileViewset(viewsets.ModelViewSet):
    queryset = GuideUserProfile.objects.all()
    serializer_class = GuideUserProfileSerializers

class AgencyUserProfileViewset(viewsets.ModelViewSet):
    queryset = TravelAgencyProfile.objects.all()
    serializer_class = TravelAgencyUserProfileSerializers
