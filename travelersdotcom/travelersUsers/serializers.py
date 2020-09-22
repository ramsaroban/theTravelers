from rest_framework import serializers
from .models import Users

class TouristUsersRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=15, min_length=7, write_only=True)
    password2 = serializers.CharField(max_length=15, min_length=7, write_only=True)

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
    password1 = serializers.CharField(max_length=15, min_length=7, write_only=True)
    password2 = serializers.CharField(max_length=15, min_length=7, write_only=True)

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




        


