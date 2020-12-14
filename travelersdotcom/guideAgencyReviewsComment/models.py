from django.db import models
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth import get_user_model
from django.db.models import Avg
Users = get_user_model()
# Create your models here.
class GuideAgencyReview(models.Model):
    user        = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='guide_agency_reviewer')
    reviewed_user    = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='guide_agency_reviewed')
    reviews     = models.TextField(_('Reviews'), max_length=1111, blank=True, null=True)
    rating      = models.FloatField(_('Rating'), max_length=5.0, default=1.0, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.reviewed_user.email)

    @property
    def average_rating(self):
    	return  GuideAgencyReview.objects.filter(reviewed_user=self.reviewed_user).aggregate(Avg('rating')).get('rating__avg')

    