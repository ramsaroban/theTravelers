from rest_framework import routers
from django.urls import path,include
from .views import *


app_name = 'travelersMedia'


router = routers.SimpleRouter()
# router.register('user', ImageModelView),\


urlpatterns = [
path('user/',ImageModelView.as_view(),name='user-image')
]
urlpatterns += router.urls