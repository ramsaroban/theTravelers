from django.db import models
from core_utility import places_images
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Banner(models.Model):
	title = models.CharField(_('Title of event'),max_length=30)
	about = models.TextField(_('Description of event'),max_length=400)
	image = models.ImageField(_('Country Pic'),upload_to = places_images, blank=True, null= True)
	host = models.CharField(_('Banner Host party'),max_length=20)
	start_time=models.DateTimeField(blank=True,null=True)
	end_time=models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.title