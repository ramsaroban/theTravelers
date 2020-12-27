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




urlpatterns = [
 path('get-by-category/<int:id>',GetVisitingPlaceByCategory.as_view(),name='get-visiting-place-by-category'),
 path('get-by-activity/<int:id>',GetVisitingPlaceByActivity.as_view(),name='get-visiting-place-by-activity'),
 path('get-near-places-by-radius/<int:id>',GetNearPlacesByRadius.as_view(),name='get-near-place-by-radius'),
]


urlpatterns += router.urls