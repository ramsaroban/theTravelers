from django.urls import path 
from .views import *


from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'travelersPlaces'


router = routers.SimpleRouter()

router.register('country', CountryView),
router.register('area', AreasView),
router.register('activities', ActivitiesAtPlacesView),
router.register('category', PlaceCategoryView),
router.register('visitingplace', TravelersVisitingPlacesView),




urlpatterns = []


urlpatterns += router.urls

