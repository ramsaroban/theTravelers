from django.urls import path 

from rest_framework import routers
from django.urls import path,include
from .views import *

app_name = 'travelersReviewComment'


router = routers.SimpleRouter()


urlpatterns = [
 path('place/create/',VisitingPlaceReviewRatingCreate.as_view(),name='visiting-place-review-rating-create'),
 path('place/update/<int:pk>/',VisitingPlaceReviewRatingUpdate.as_view(),name='visiting-place-review-rating-update'),
 path('get-place-review/by-place/<int:id>/',GetVisitingPlaceReviewRatingByPlace.as_view(),name='get-place-review-rating-by-place'),
 path('get-place-review/by-user/<int:id>',GetVisitingPlaceReviewRatingByUser.as_view(),name='get-place-review-rating-by-user'),

 path('guide-agency-review/create/',GuideAgencyReviewsCommentCreate.as_view(),name='guide-agency-review-rating-create'),
 path('guide-agency-review/update/<int:pk>/',GuideAgencyReviewsCommentUpdate.as_view(),name='guide-agency-review-rating-update'),
]
urlpatterns += router.urls
