
from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    TouristUserRegisterView,
    GuideAndTravelAgencyUserRegisterView,
    VerifyEmail,
    LoginAPIView,
    RequestPasswordResetEmail,
    ValidatePasswordResetTokenView,
    SetUpdatePasswordAPIView,
    )

urlpatterns = [
    path('user/register', TouristUserRegisterView.as_view(), name='user-register'),
    path('partners/register', GuideAndTravelAgencyUserRegisterView.as_view(), name='partners-register'),
    path('verify-email', VerifyEmail.as_view(), name='verify-email'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-password', RequestPasswordResetEmail.as_view(), name='request-reset-password'),
    path('reset-password/<uidb64>/<token>', ValidatePasswordResetTokenView.as_view(), name='reset-password-confirm'),
    path('reset-password-complete', SetUpdatePasswordAPIView.as_view(), name='reset-password-complete'),
]
