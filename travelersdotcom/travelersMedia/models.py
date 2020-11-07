from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
Users = get_user_model()
from core_utility import  image_directory_path

from travelersPlaces.models import (
    TravelersVisitingPlaces
)

class PlaceImageModel(models.Model):

    options = (
        ('active','Active'),
        ('deactivated','Deactivated'),
    )
    uploader        = models.ForeignKey(Users, related_name='users_photo', blank=True, on_delete=models.CASCADE)
    place           = models.ForeignKey(TravelersVisitingPlaces, on_delete=models.CASCADE, related_name='place_images', blank=True, null=True)
    title           = models.CharField(max_length=555)
    alt             = models.CharField(null=True, blank=True, max_length=255)
    image           = models.ImageField(upload_to=image_directory_path, default = 'images/static/defualt.png')
    uploaded_date   = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(max_length=15, choices=options, default=options[0])

    def __str__(self):
        return '{}'.format(self.image)

