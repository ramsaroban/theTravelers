
from django.urls import path 
from .views import (
    TouristUserRegisterView,
    GuideAndTravelAgencyUserRegisterView
    )

urlpatterns = [
    path('user/register', TouristUserRegisterView.as_view(), name='user-register'),
    path('partners/register', GuideAndTravelAgencyUserRegisterView.as_view(), name='partners-register'),
    #path('user/register', GuideAndTravelAgencyUserRegisterView.as_view(), name='user-register'),
]
