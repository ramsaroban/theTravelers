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
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
Users = get_user_model()


def modify_input_for_multiple_files(user_id,title,alt,image,status,):
    dict = {}
    dict['user'] = user_id
    dict['title'] = title
    dict['alt'] = alt
    dict['image'] = image
    dict['status'] = status
    return dict

class ImageModelView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request, *args, **kwargs):
        user = request.data['user']
        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        alt=request.data['alt']
        _status=request.data['status']
        title=request.data['title']
    
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(user,title,alt,img_name,_status)
          
            file_serializer = ImageModelSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)

 