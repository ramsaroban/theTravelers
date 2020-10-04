from django.shortcuts import render
from .serializers import (
    ImageModelSerializer,
)

from .models import (
    ImageModel,
  
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

Users = get_user_model()

class ImageModelView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post','put','delete']

    