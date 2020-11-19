  
from rest_framework import serializers

from .models import TravelersVisitingPlaceReviewsComment
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