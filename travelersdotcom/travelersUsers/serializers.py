from rest_framework import serializers
from .models import Users
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes,smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

class TouristUsersRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, min_length=7, write_only=True)
    password2 = serializers.CharField(max_length=30, min_length=7, write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password1', 'password2']

    def validate(self, attrs):
        user_email = attrs.get('email','')
        if not user_email:
            raise serializers.ValidationError('User must have an Email address')

        first_name = attrs.get('first_name','')

        if not first_name:
            raise serializers.ValidationError('User must have first name')
        
        last_name = attrs.get('last_name','')

        if not last_name:
            raise serializers.ValidationError('User must have last name')
        
        password1 = attrs.get('password1','')
        password2 = attrs.get('password2','')

        if password1 != password2:
            raise serializers.ValidationError('Password does not match!')
        
        attrs.pop('password1')
        attrs.pop('password2')
        attrs['password'] = password1

        return attrs
    
    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class GuideAndTravelAgencyUsersRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, min_length=7, write_only=True)
    password2 = serializers.CharField(max_length=30, min_length=7, write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password1', 'password2','user_type']

    def validate(self, attrs):
        user_email = attrs.get('email','')
        if not user_email:
            raise serializers.ValidationError('User must have an Email address')

        user_type = attrs.get('user_type','')
        if not user_type:
            raise serializers.ValidationError('User must select either of [Guide/Travel Agenecy]')

        first_name = attrs.get('first_name','')
        if not first_name:
            raise serializers.ValidationError('User must have first name')
        
        last_name = attrs.get('last_name','')

        if not last_name:
            raise serializers.ValidationError('User must have last name')
        
        password1 = attrs.get('password1','')
        password2 = attrs.get('password2','')

        if password1 != password2:
            raise serializers.ValidationError('Password doesnt match')
        
        attrs.pop('password1')
        attrs.pop('password2')
        attrs['password'] = password1
        return attrs
    
    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class EmailVerificationSerializers(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Users
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30, min_length=7, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    refreshToken = serializers.CharField(max_length=555, read_only=True)
    accessToken = serializers.CharField(max_length=555, read_only=True)

    class Meta:
        model = Users
        fields = ['email','first_name','password','refreshToken','accessToken']

    # def get_token(self,obj):
    #     user = Users.objects.get(email=obj['email'])

    #     return

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credential, try with valid credentials.')
        if not user.is_active:
            raise AuthenticationFailed('Account is not active, please contact at help@thetraveler.com')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified.')

        tokens = user.tokens()

        data = {
            'email':user.email,
            'first_name':user.first_name,
            'refreshToken':tokens.get('refresh'),
            'accessToken':tokens.get('access'),
        }
        return  data

class ResetPasswordRequestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)

    class Meta:
        model = Users
        fields = ['email']

class ValidatePasswordResetTokenViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = []

class SetUpdatePasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=30, min_length=7, write_only=True) 
    password2 = serializers.CharField(max_length=30, min_length=7, write_only=True) 
    uidb64 = serializers.CharField(max_length=15, write_only=True) 
    token = serializers.CharField(max_length=555, write_only=True) 
    
    class Meta:
        model = Users
        fields = ['password1','password2','uidb64','token']
    def validate(self, attrs):
        try:
            password1 = attrs.get('password1','')
            password2 = attrs.get('password2','')
            uidb64 = attrs.get('uidb64','')
            token = attrs.get('token','')
            if password1 != password2:
                raise AuthenticationFailed('Password does not match.',401)

            id = force_str(urlsafe_base64_decode(uidb64))
            user = Users.objects.get(id=id)
            if not user:
                raise AuthenticationFailed('Invalid token or uidb64.',401)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('Password reset link is invalid.',401)

            user.set_password(password1)
            user.save()
            return (user)
        except Exception as identifier:
            #raise AuthenticationFailed('Password reset link is invalid.',401)
            raise identifier


        return super().validate(attrs)