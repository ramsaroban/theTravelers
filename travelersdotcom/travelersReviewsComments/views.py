from django.shortcuts import render
from .serializers import (
    TravelersVisitingPlaceReviewsCommentSerializers,
    TravelersVisitingPlaceReviewsCommentUpdateSerializers
)

from .models import (
    TravelersVisitingPlaceReviewsComment,
  
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
Users = get_user_model()
from rest_framework.generics import CreateAPIView,UpdateAPIView

from django.shortcuts import get_object_or_404

from rest_framework import permissions




class LocationReviewRatingCreate(CreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class=TravelersVisitingPlaceReviewsCommentSerializers
	def create(self, request, *args, **kwargs):
		if int(request.user.id) == int(request.data['user']):
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			self.perform_create(serializer)
			headers = self.get_success_headers(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
		else:
			return Response({'detail':'Not allowded to make others review.'})



class LocationReviewRatingUpdate(UpdateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class=TravelersVisitingPlaceReviewsCommentUpdateSerializers
	http_method_names = ['put']

	
	def update(self, request, *args, **kwargs):
		if int(request.user.id) == int(request.data['user']):
			partial = kwargs.pop('partial', False)
			instance = get_object_or_404(TravelersVisitingPlaceReviewsComment,id=kwargs['pk'])
			serializer = self.get_serializer(instance, data=request.data, partial=partial)
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)

			if getattr(instance, '_prefetched_objects_cache', None):
			    instance._prefetched_objects_cache = {}

			return Response(serializer.data)
		else:
			return Response({'detail':'Not allowded to update others review.'})

	
	