from django.shortcuts import render
from .serializers import *

from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission,SAFE_METHODS
from rest_framework.generics import ListAPIView
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

Users = get_user_model()
from django.shortcuts import get_object_or_404

from .permissions import PlacePermission


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


class GetVisitingPlaceByCategory(ListAPIView):
    queryset = TravelersVisitingPlaces.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=TravelersVisitingPlacesSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = TravelersVisitingPlaces.objects.filter(category=self.kwargs['id'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GetVisitingPlaceByActivity(ListAPIView):
    queryset = TravelersVisitingPlaces.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=TravelersVisitingPlacesSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = TravelersVisitingPlaces.objects.filter(activites=self.kwargs['id'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class GetNearPlacesByRadius(ListAPIView):
    queryset = TravelersVisitingPlaces.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class=TravelersVisitingPlacesSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        current_place_radius=request.data.get('radius',None)
        queryset = TravelersVisitingPlaces.objects.filter(location__distance_lt=(current_place_radius,Distance(km=5)))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)