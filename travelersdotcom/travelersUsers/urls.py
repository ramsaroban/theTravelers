
from django.urls import path 
from .views import (
    TouristUserRegisterView,
    GuideAndTravelAgencyUserRegisterView,
    VerifyEmail,
    TouristUserProfileViewset,
    )



from rest_framework import routers
from django.urls import path,include
from .views import *

app_name = 'travelersUser'


router = routers.SimpleRouter()
router.register('touristprofile', TouristUserProfileViewset),

urlpatterns = [
    path('user/register', TouristUserRegisterView.as_view(), name='user-register'),
    path('partners/register', GuideAndTravelAgencyUserRegisterView.as_view(), name='partners-register'),
    path('verify-email', VerifyEmail.as_view(), name='verify-email'),
]
urlpatterns += router.urls
