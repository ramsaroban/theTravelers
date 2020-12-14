from django.urls import path 

from rest_framework import routers
from django.urls import path,include
from .views import *

app_name = 'guideAgencyReviewsComment'


router = routers.SimpleRouter()


urlpatterns = [
 path('create/',guideAgencyReviewsCommentCreate.as_view(),name='guide-agency-review-rating-create'),
 path('update/<int:pk>/',guideAgencyReviewsCommentUpdate.as_view(),name='guide-agency-review-rating-update'),
 
]
urlpatterns += router.urls
