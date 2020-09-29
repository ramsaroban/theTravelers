from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'userProfile'


router = routers.SimpleRouter()
router.register('touristprofile', TouristUserProfileViewset),
router.register('guideprofile', GuideUserProfileViewset),
router.register('agencyprofile', AgencyUserProfileViewset),

urlpatterns = [
path('touristprofile/', TouristUserProfileViewset.as_view({
    'post': 'create'
})),
path('guideprofile/', GuideUserProfileViewset.as_view({
    'post': 'create'
})),

path('agencyprofile/', AgencyUserProfileViewset.as_view({
    'post': 'create'
})),


]
urlpatterns += router.urls