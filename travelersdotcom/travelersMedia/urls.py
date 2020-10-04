from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'travelersMedia'


router = routers.SimpleRouter()
router.register('user', ImageModelView),


urlpatterns = []
urlpatterns += router.urls