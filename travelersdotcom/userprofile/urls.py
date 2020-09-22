from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'userProfile'


router = routers.SimpleRouter()
router.register('touristprofile', TouristUserProfileViewset),
router.register('guideprofile', GuideUserProfileViewset),
router.register('agencyprofile', AgencyUserProfileViewset),

urlpatterns = []
urlpatterns += router.urls