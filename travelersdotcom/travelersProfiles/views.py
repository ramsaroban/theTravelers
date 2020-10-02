from django.shortcuts import render
from .serializers import (
    TouristProfileSerializer,
    GuideUserProfileSerializer,
    TravelAgencyUserProfileSerializer,
)

from .models import (
    TouristUserProfile,
    GuideUserProfile,
    TravelAgencyProfile
)
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

Users = get_user_model()

class TouristProfileView(viewsets.ModelViewSet):
    queryset = TouristUserProfile.objects.all()
    serializer_class = TouristProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

class GuideUserProfileViewset(viewsets.ModelViewSet):
    queryset = GuideUserProfile.objects.all()
    serializer_class = GuideUserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

class AgencyUserProfileViewset(viewsets.ModelViewSet):
    queryset = TravelAgencyProfile.objects.all()
    serializer_class = TravelAgencyUserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")