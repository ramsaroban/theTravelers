from django.shortcuts import render
from .serializers import (
    GuideAgencyReviewsCommentCreateSerializer,
    GuideAgencyReviewsCommentUpdateSerializer
    
)

from .models import (
    GuideAgencyReview,
  
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
Users = get_user_model()
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView

from django.shortcuts import get_object_or_404

from rest_framework import permissions

class guideAgencyReviewsCommentCreate(CreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class=GuideAgencyReviewsCommentCreateSerializer
	def create(self, request, *args, **kwargs):
		
		if int(request.user.id) == int(request.data['user']):
			print(request.data)
			serializer = self.get_serializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			self.perform_create(serializer)
			headers = self.get_success_headers(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
		else:
			return Response({'error':'Not Allowed to Create'}, status=status.HTTP_400_BAD_REQUEST)



class guideAgencyReviewsCommentUpdate(UpdateAPIView):
	queryset = GuideAgencyReview.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class=GuideAgencyReviewsCommentUpdateSerializer
	http_method_names = ['put']

	
	def update(self, request, *args, **kwargs):
		if int(request.user.id) == int(request.data['user']):
			partial = kwargs.pop('partial', False)
			instance = get_object_or_404(GuideAgencyReview,id=kwargs['pk'])
			serializer = self.get_serializer(instance, data=request.data, partial=partial)
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)

			if getattr(instance, '_prefetched_objects_cache', None):
			    instance._prefetched_objects_cache = {}

			return Response(serializer.data)
		else:
			return Response({'error':'Not allowded to Update'}, status=status.HTTP_400_BAD_REQUEST)
