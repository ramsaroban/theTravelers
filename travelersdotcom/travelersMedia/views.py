from django.shortcuts import render
from .serializers import (
    ImageModelSerializer,
)

from .models import (
    PlaceImageModel,
  
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
Users = get_user_model()



def modify_input_for_multiple_files(user_id,place,title,alt,image,status):
    dict = {}
    dict['uploader'] = user_id
    dict['place'] = place
    dict['title'] = title
    dict['alt'] = str(image)
    dict['image'] = image
    dict['status'] = 'active'
    return dict

class ImageListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        queryset=PlaceImageModel.objects.filter(uploader=request.user.id)
        serializer=ImageModelSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        user = request.data['user']

        images = dict((request.data).lists())['image']
        alt=_status=None
        title=request.data['title']
        place=request.data['place']

    
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(user,place,title,alt,img_name,_status)
          
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


class ImageDetailView(APIView):
    """
    Retrieve, update or delete a image instance.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return PlaceImageModel.objects.get(pk=pk)
        except PlaceImageModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageModelSerializer(image)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)