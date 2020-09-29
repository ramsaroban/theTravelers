from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import *
from .serializers import *

class TouristUserProfileViewset(viewsets.ModelViewSet):
    queryset = TouristUserProfile.objects.all()
    serializer_class = TouristUserProfileSerializers
    http_method_names = ['get', 'post','put','delete','head']
    
class GuideUserProfileViewset(viewsets.ModelViewSet):
    queryset = GuideUserProfile.objects.all()
    serializer_class = GuideUserProfileSerializers
    http_method_names = ['get', 'post','put','delete','head']

class AgencyUserProfileViewset(viewsets.ModelViewSet):
    queryset = TravelAgencyProfile.objects.all()
    serializer_class = TravelAgencyUserProfileSerializers
    http_method_names = ['get', 'post','put','delete','head']
