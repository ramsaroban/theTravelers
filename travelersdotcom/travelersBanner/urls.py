from django.urls import path 
from .views import *
from rest_framework import routers
from django.urls import path,include

app_name = 'travelersBanner'

router = routers.SimpleRouter()

router.register('', BannerView),

urlpatterns = [
]
urlpatterns += router.urls