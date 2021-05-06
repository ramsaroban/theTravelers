from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.db.models import Avg
User = get_user_model()

from travelersPlaces.models import (
    TravelersVisitingPlaces,
)

class TravelersVisitingPlaceReviewsComment(models.Model):
    user        = models.ForeignKey(User, on_delete=models.PROTECT, related_name='place_review_user')
    place       = models.ForeignKey(TravelersVisitingPlaces, on_delete=models.CASCADE, related_name='place_reviews')
    reviews     = models.TextField(_('Reviews'), max_length=1111, blank=True, null=True)
    rating      = models.FloatField(_('Rating'), max_length=5.0, default=1.0, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.place.name)
    
    @property
    def average_rating_place(self):
    	return  TravelersVisitingPlaceReviewsComment.objects.filter(place=self.place).aggregate(Avg('rating')).get('rating__avg')

# Create your models here.
class GuideAgencyReview(models.Model):
    user        = models.ForeignKey(User, on_delete=models.PROTECT, related_name='guide_agency_reviewer')
    reviewed_user    = models.ForeignKey(User, on_delete=models.PROTECT, related_name='guide_agency_reviewed')
    reviews     = models.TextField(_('Reviews'), max_length=1111, blank=True, null=True)
    rating      = models.FloatField(_('Rating'), max_length=5.0, default=1.0, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.reviewed_user.email)

    @property
    def average_rating(self):
        return  GuideAgencyReview.objects.filter(reviewed_user=self.reviewed_user).aggregate(Avg('rating')).get('rating__avg')

