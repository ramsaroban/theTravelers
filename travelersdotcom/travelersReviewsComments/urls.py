from django.urls import path 

from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'travelersReviewComment'


router = routers.SimpleRouter()


urlpatterns = [
 path('locations/create/',LocationReviewRatingCreate.as_view(),name='location-review-rating-create'),
 path('locations/update/<int:pk>/',LocationReviewRatingUpdate.as_view(),name='location-review-rating-update'),



]
urlpatterns += router.urls