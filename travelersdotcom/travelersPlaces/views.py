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



class PlacePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        else:
        	user=get_object_or_404(Users,id=request.user.id)
        	if request.method in SAFE_METHODS and (user.is_staff or user.is_superuser or user.is_admin):
        		return True
        	else:
        		if user.is_staff or user.is_superuser or user.is_admin:
        			return True
        		else:
        			return False

class CountryView(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,PlacePermission]
    http_method_names = ['get', 'post','put','delete']


class AreasView(viewsets.ModelViewSet):
    queryset = AreasModel.objects.all()
    serializer_class = AreasModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,PlacePermission]
    http_method_names = ['get', 'post','put','delete']


class ActivitiesAtPlacesView(viewsets.ModelViewSet):
    queryset = ActivitiesAtPlacesModel.objects.all()
    serializer_class = ActivitiesAtPlacesModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,PlacePermission]
    http_method_names = ['get', 'post','put','delete']


class PlaceCategoryView(viewsets.ModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,PlacePermission]
    http_method_names = ['get', 'post','put','delete']


class TravelersVisitingPlacesView(viewsets.ModelViewSet):
    queryset = TravelersVisitingPlaces.objects.all()
    serializer_class = TravelersVisitingPlacesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,PlacePermission]
    http_method_names = ['get', 'post','put','delete']
    