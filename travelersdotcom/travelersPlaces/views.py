from django.shortcuts import render
from .serializers import *

from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission,SAFE_METHODS

Users = get_user_model()
from django.shortcuts import get_object_or_404

from .permissions import PlacePermission


class CountryView(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']


class AreasView(viewsets.ModelViewSet):
    queryset = AreasModel.objects.all()
    serializer_class = AreasModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']


class ActivitiesAtPlacesView(viewsets.ModelViewSet):
    queryset = ActivitiesAtPlacesModel.objects.all()
    serializer_class = ActivitiesAtPlacesModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']


class PlaceCategoryView(viewsets.ModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']


class TravelersVisitingPlacesView(viewsets.ModelViewSet):
    queryset = TravelersVisitingPlaces.objects.all()
    serializer_class = TravelersVisitingPlacesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']