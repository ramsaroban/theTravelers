from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import ( 
    TouristUsersRegisterSerializer,
    GuideAndTravelAgencyUsersRegisterSerializer,
)

from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class TouristUserRegisterView(generics.GenericAPIView):
    serializer_class = TouristUsersRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = Users.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        absUrl = 'http://'+current_site+relativeLink+'?toekn='+str(token)

        email_body = 'Dear '+user.first_name +' '+user.last_name+ ', \n' + 'We welcome you to the travelers family. We help the traveler\'s journey easy.\nPlease click the link below to verify your email.\n Link: '+absUrl +'\n\n Regards,\nTravelers.com Family'
        
        data = {'to_email':user.email,'email_subject':'Verify your email!', 'email_body':email_body}
        Utils.send_mail(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class GuideAndTravelAgencyUserRegisterView(generics.GenericAPIView):
    serializer_class = GuideAndTravelAgencyUsersRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)



class VerifyEmail(generics.GenericAPIView):

    def get(self):
        pass