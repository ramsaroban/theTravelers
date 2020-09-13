from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response

from .serializers import ( 
    TouristUsersRegisterSerializer,
    GuideAndTravelAgencyUsersRegisterSerializer,
    EmailVerificationSerializers,
)

from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users
from .utils import Utils, UserDoesNotExistsException
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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
        absUrl = 'http://'+current_site+relativeLink+'?token='+str(token)

        email_body = 'Dear '+user.first_name +' '+user.last_name+ ', \n' + 'We welcome you to the travelers family. We made the traveler\'s journey easy.\nPlease click the link below to verify your email.\n Link: '+absUrl +'\n\n Regards,\nTravelers.com Family'
        
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

        user = Users.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        absUrl = 'http://'+current_site+relativeLink+'?token='+str(token)

        email_body = 'Dear '+user.first_name +' '+user.last_name+ ', \n' + 'Thank you for registering your bussiness as '+ user.user_type +'.\nPlease click the link below to verify your email.\n Link: '+absUrl +'\n\n Regards,\nTravelers.com Family'
        
        data = {'to_email':user.email,'email_subject':'Verify your email!', 'email_body':email_body}
        Utils.send_mail(data)

        return Response(user_data, status=status.HTTP_201_CREATED)



class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializers

    token_param_config = openapi.Parameter('token',in_=openapi.IN_QUERY, descreption='email-verify', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Users.objects.get(id=payload['user_id'])
            if not user:
                raise UserDoesNotExistsException('User doesnt exist!')
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'email':'Successfully activated your account!'}, status=status.HTTP_200_OK)
            else:
                return Response({'email':'Already Verified'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignature as idenitfier:
            return Response({'error':'Activation Key Expired'}, status=status.HTTP_400_BAD_REQUEST) 
        except jwt.DecodeError as idenitfier:
            return Response({'error':'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidSignatureError as idenitfier:
            return Response({'error':'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)
        except UserDoesNotExistsException as idenitfier:
            return Response({'error':'Invalid User'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'%s'%e}, status=status.HTTP_400_BAD_REQUEST)

