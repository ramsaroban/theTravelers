from django.db import models
from core_utility import places_images
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Banner(models.Model):
	title = models.CharField(_('Title of event'),max_length=30)
	about = models.TextField(_('Description of event'),max_length=400)
	image = models.ImageField(_('Country Pic'),upload_to = places_images, blank=True, null= True)
	
