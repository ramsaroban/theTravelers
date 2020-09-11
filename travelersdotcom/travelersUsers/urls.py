
from django.urls import path 
from .views import (
    TouristUserRegisterView,
    GuideAndTravelAgencyUserRegisterView,
    VerifyEmail,
    )

urlpatterns = [
    path('user/register', TouristUserRegisterView.as_view(), name='user-register'),
    path('partners/register', GuideAndTravelAgencyUserRegisterView.as_view(), name='partners-register'),
    path('verify-email', VerifyEmail.as_view(), name='verify-email'),
]
