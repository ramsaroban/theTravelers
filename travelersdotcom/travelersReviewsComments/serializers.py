  
from rest_framework import serializers

from .models import (
	TravelersVisitingPlaceReviewsComment,
	GuideAgencyReview
)

from django.contrib.auth import get_user_model
Users = get_user_model()
from rest_framework.fields import CurrentUserDefault

class TravelersVisitingPlaceReviewsCommentSerializers(serializers.ModelSerializer):
	average_rating_place=serializers.ReadOnlyField()
	
	def validate_rating(self,value):
		if value < 1 or value > 5:
			raise serializers.ValidationError("Invalid rating point.Point must be grater or equal to 1 and less than equal to 5.")
		return value
	
	def validate_user(self,value):
		if TravelersVisitingPlaceReviewsComment.objects.filter(user=value):
			raise serializers.ValidationError("You have already rated this place.")
		return value

	class Meta:
		model = TravelersVisitingPlaceReviewsComment
		fields = ['user','place','reviews','rating','average_rating_place',]

class TravelersVisitingPlaceReviewsCommentUpdateSerializers(serializers.ModelSerializer):
	average_rating_place=serializers.ReadOnlyField()
	
	def validate_rating(self,value):
		if value < 1 or value > 5:
			raise serializers.ValidationError("Invalid rating point.Point must be grater or equal to 1 and less than equal to 5.")
		return value
	
	class Meta:
		model = TravelersVisitingPlaceReviewsComment
		fields = ['user','place','reviews','rating','average_rating_place',]


class GetVisitingPlaceReviewRatingByPlaceSerializer(serializers.ModelSerializer):
	average_rating_place=serializers.ReadOnlyField()
	class Meta:
		model=TravelersVisitingPlaceReviewsComment
		fields = ['user','place','reviews','rating','average_rating_place',]


class GuideAgencyReviewsCommentCreateSerializer(serializers.ModelSerializer):
	average_rating=serializers.ReadOnlyField()
	
	def validate_rating(self,value):
		if value < 1 or value > 5:
			raise serializers.ValidationError("Invalid rating point.Point must be grater or equal to 1 and less than equal to 5.")
		return value
	
	def validate_user(self,value):
		if Users.objects.filter(email=value,user_type='Tourist'):
			return value
		raise serializers.ValidationError("Only tourist can rate guide or agency.")
	
	def reviewed_user(self,value):
		if Users.objects.filter(Q(email=value) & Q(Q(user_type='Guide') | Q(user_type='Travel Agency'))):
			return value
		raise serializers.ValidationError("Only guide and travel agency can be reviewed or can be rated.")

	def validate(self,attrs):
		user=attrs.get('user','')
		reviewed_user=attrs.get('reviewed_user','')
		if GuideAgencyReview.objects.filter(user=user,reviewed_user=reviewed_user):
			raise serializers.ValidationError("You have already rated this tourist/guide.")
		return attrs


	class Meta:
		model = GuideAgencyReview
		fields = ['user','reviewed_user','reviews','rating','average_rating',]

class GuideAgencyReviewsCommentUpdateSerializer(serializers.ModelSerializer):
	average_rating=serializers.ReadOnlyField()
	
	def validate_rating(self,value):
		if value < 1 or value > 5:
			raise serializers.ValidationError("Invalid rating point.Point must be grater or equal to 1 and less than equal to 5.")
		return value
	
	class Meta:
		model = GuideAgencyReview
		fields = ['user','reviewed_user','reviews','rating','average_rating',]