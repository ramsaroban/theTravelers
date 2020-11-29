from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
from django.core.serializers import serialize
User = get_user_model()

from django.utils.translation import ugettext_lazy as _

from core_utility import places_images
# from travelersReviewsComments.models import(
#     TravelersVisitingPlaceReviewsComment,
# )
from django.db.models import Avg


class TravelersUserLocation(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_location')
    location       = models.PointField(default='POINT(0,0)', srid=4326)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    @property
    def longitude(self):
        return self.location[0]
    
    @property
    def latitude(self):
        return self.location[1]

    def __str__(self):
        return '{}'.format(self.user)

class CountryModel(models.Model):
    name = models.CharField(_('Country Name'), max_length = 100)
    image = models.ImageField(_('Country Pic'),upload_to = places_images, blank=True, null= True)
    description = models.TextField(_('About Countary'), max_length=5555, blank=True, null=True)
    location =  models.PointField(default='POINT(0,0)', srid=4326)

    @property
    def longitude(self):
        return self.location[0]
    
    @property
    def latitude(self):
        return self.location[1]

    def __str__(self):
        return '{}'.format(self.name)

class AreasModel(models.Model):
    country     = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='country_local_areas')
    name        = models.CharField(_('City Name'), max_length=255, blank = True, null = True)
    description = models.TextField(_('About Area'), max_length=5555, blank=True,null=True)
    image       = models.ImageField(_('Logo Image'), upload_to=places_images, blank=True, null=True)
    location    = models.PointField(_('Location'),default='POINT(0,0)', srid=4326)

    @property
    def longitude(self):
        return self.location[0]
    
    @property
    def latitude(self):
        return self.location[1]

    def __str__(self):
        return '{}'.format(self.name)

class ActivitiesAtPlacesModel(models.Model):
    name    = models.CharField(_('Activities Name'), max_length=55, unique=True)
    image   = models.ImageField(_('Image'), upload_to=places_images, blank=True, null=True)

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
    category    = models.CharField(_('Category Name'), max_length=55, unique = True)
    image       = models.ImageField(_('Image'), upload_to=places_images, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.category)


class TravelersVisitingPlaces(models.Model):
    local_area  = models.ForeignKey(AreasModel, on_delete=models.PROTECT, related_name='local_area_place')
    name        = models.CharField(_('Title'), max_length=255)
    about       = models.TextField(_('Ábout'),  max_length=5555)
    image       = models.ImageField(_('Logo Image'),upload_to=places_images, blank=False, null=False)
    category    = models.ManyToManyField(PlaceCategory, related_name='place_category')
    activites   = models.ManyToManyField(ActivitiesAtPlacesModel, related_name='place_activity')
    location    = models.PointField(_('Visiting Place Location'), default='POINT(0,0)', blank=True, null=True)

    def __str__(self):
       return '{}'.format(self.name) 
    
    @property
    def longitude(self):
        return self.location[0]
    
    @property
    def latitude(self):
        return self.location[1]
    
    @property
    def reviews(self):
        data = {}
        reviews_count = self.place_reviews.filter(place = self.id).count()
        rating_average = self.place_reviews.aggregate(Avg('rating')).get('rating__avg')
        data['total_reviews'] = reviews_count
        data['avg_rating'] =  rating_average
        return data
    @property
    # def reviews_all(self):
    #     data = self.place_reviews
    @property
    def locality(self):
        area = AreasModel.objects.get(id=self.id)
        data = {}
        data['id'] = area.id
        data['name'] = area.name
        return data
    
    @property
    def categories(self):
        data = PlaceCategory.objects.filter(place_category=self.id).values_list('category')
        return data
    
    @property
    def activities(self):
        data = ActivitiesAtPlacesModel.objects.filter(place_activity=self.id).values_list('name')
        return data