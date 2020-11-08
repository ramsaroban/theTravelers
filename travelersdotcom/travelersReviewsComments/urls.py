from django.urls import path 

from rest_framework import routers
from django.urls import path,include
from .views import (
    LocationReviewRatingCreate,
    LocationReviewRatingUpdate,
)


app_name = 'travelersReviewComment'


router = routers.SimpleRouter()


urlpatterns = [
 path('place/create/',LocationReviewRatingCreate.as_view(),name='location-review-rating-create'),
 path('place/update/<int:pk>/',LocationReviewRatingUpdate.as_view(),name='location-review-rating-update'),



]
urlpatterns += router.urls
