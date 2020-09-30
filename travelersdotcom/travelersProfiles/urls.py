from django.urls import path 
from .views import (
    TouristProfileView,
    )

# urlpatterns = [
#     path('create', TouristProfileView.as_view({'post':'create'}), name='tourist-profile'),
#     path('update', TouristProfileView.as_view({'patch':'update'}), name='tourist-profile-update'),
#     path('put', TouristProfileView.as_view({'put':'put'}), name='tourist-profile-put'),
# ]

  
from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'travelersProfiles'


router = routers.SimpleRouter()
router.register('touristprofile', TouristProfileView),
router.register('guideprofile', GuideUserProfileViewset),
router.register('agencyprofile', AgencyUserProfileViewset),

urlpatterns = []
urlpatterns += router.urls