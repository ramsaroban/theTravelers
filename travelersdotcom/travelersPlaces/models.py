from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.translation import ugettext_lazy as _

from core_utility import places_images




class TravelersLocation(models.Model):
    label   = models.CharField(_('Label'), max_length=255)
    slug    = models.SlugField(_('Slug'), blank=True, null=True) 
    point = models.PointField(default='POINT(0,0)', srid=4326)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def longitude(self):
        return self.point[0]
    
    @property
    def latitude(self):
        return self.point[1]



class CountryModel(models.Model):
    name = models.CharField(_('Countary Name'), max_length = 100)
    image = models.ImageField(_('Countary Pic'),upload_to = places_images, blank=True, null= True)
    description = models.TextField(_('About Countary'), max_length=5555, blank=True, null=True)
    location =  models.PointField(default='POINT(0,0)', srid=4326)

    def __str__(self):
        return '{}'.format(self.name)

class AreasModel(models.Model):
    country    = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='local_areas')
    city_name   = models.CharField(_('City Name'), max_length=255, blank = True, null = True)
    description = models.TextField(_('About Area'), max_length=5555, blank=True,null=True)
    logo_image  = models.ImageField(_('Logo Image'), upload_to=places_images, blank=True, null=True)
    location    = models.PointField(_('Location'),default='POINT(0,0)', srid=4326)

    def __str__(self):
        return '{}'.format(self.city_name)

class ActivitiesAtPlacesModel(models.Model):
    name = models.CharField(_('Activities Name'), max_length=55, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


# PLACE_CATEGORY =(
#     ('historical','Historical'),
#     ('religious','Religous'),
#     ('theme park','Theme Park'),
#     ('zoo park','Zoo Park'),
#     ('adventure park','Adventure Park'),
#     ('adventure sports','Adventure sports'),
#     ('trekking','Trekking'),
#     ('kids park','Kid Park'),
#     ('art & culture','Art & Culture'),
#     ('museums','Museums'),
# )

class PlaceCategory(models.Model):
    category = models.CharField(_('Category Name'), max_length=55, unique = True)

    def __str__(self):
        return '{}'.format(self.category)

class TravelersVisitingPlaces(models.Model):
    local_area  = models.ForeignKey(AreasModel, on_delete=models.PROTECT, related_name='local_area_place')
    name       = models.CharField(_('Title'), max_length=255)
    about       = models.TextField(_('Ábout'),  max_length=5555)
    logo_image  = models.ImageField(_('Logo Image'),upload_to=places_images, blank=False, null=False)
    category  = models.ManyToManyField(PlaceCategory, related_name='place_category',blank=True,null=True)
    activites   = models.ManyToManyField(ActivitiesAtPlacesModel, related_name='place_activity', blank=True, null=True)
    location    = models.PointField(_('Visiting Place Location'), default='POINT(0,0)', blank=True, null=True)

    def __str__(self):
       return '{}'.format(self.name) 