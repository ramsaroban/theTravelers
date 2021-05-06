from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import BannerPermission


class BannerView(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,BannerPermission]
    http_method_names = ['get', 'post','put','delete']