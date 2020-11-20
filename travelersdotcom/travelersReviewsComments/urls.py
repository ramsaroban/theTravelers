from django.urls import path 

from rest_framework import routers
from django.urls import path,include
from .views import (
    LocationReviewRatingCreate,
    LocationReviewRatingUpdate,
    GetLocationReviewRatingByPlace,
    GetLocationReviewRatingByUser,
)


app_name = 'travelersReviewComment'


router = routers.SimpleRouter()


urlpatterns = [
 path('place/create/',LocationReviewRatingCreate.as_view(),name='location-review-rating-create'),
 path('place/update/<int:pk>/',LocationReviewRatingUpdate.as_view(),name='location-review-rating-update'),
 path('get/review/by/location/',GetLocationReviewRatingByPlace.as_view(),name='get-review-rating-by-place'),
 path('get/review/by/user/',GetLocationReviewRatingByUser.as_view(),name='get-review-rating-by-user'),


]
urlpatterns += router.urls
