from django.contrib import admin
from .models import (
    TouristUserProfile,
    GuideUserProfile,
    TravelAgencyProfile,
)

admin.site.register(TouristUserProfile)
admin.site.register(GuideUserProfile)
admin.site.register(TravelAgencyProfile)
# Register your models here.
