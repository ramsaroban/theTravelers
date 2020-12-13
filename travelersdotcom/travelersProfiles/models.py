from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _ 
from core_utility import (
    image_directory_path,
    profile_image_directory_path,
    passport_image_directory_path,
    visa_image_directory_path,
    gov_id_image_directory_path,
    police_verification_image_directory_path,
    agreement_image_directory_path,
)
#from travelersMedia.models import ImageModel 

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
Users = get_user_model()


#Gender Choices 
GENDER_CHOICES = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Others','OTHERS')
)
#Visitors(Tourist Profiles)
class TouristUserProfile(models.Model):
    user            = models.OneToOneField(Users, primary_key=True, on_delete=models.CASCADE, related_name='tourist_user_profile')
    mobile_number   = models.CharField(_('Phone Number'),max_length=15, blank=False, help_text="Contact Phone Number")
    gender          = models.CharField(max_length=10,
                                       choices=GENDER_CHOICES,
                                       default=GENDER_CHOICES[0][0])
    date_of_birth   = models.DateField()
    nationality     = models.CharField(_('Nationality'), max_length=30, blank=False, null=False)
    profile_pic     = models.ImageField(_('Profile Pic'),upload_to=profile_image_directory_path, blank=True, null=True)
    passport_image  = models.ImageField(_('Passpoer Image'),upload_to=passport_image_directory_path, blank=True, null=True)
    visa_image      = models.ImageField(_('Visa Image'),upload_to= visa_image_directory_path, blank=True, null=True)
    #photos          = models.ManyToManyField(ImageModel, related_name='tourist_users_photo', blank=True)

    def __str__(self):
        return self.user.email 


GUIDE_TYPE_CHOICES=(
    ('ALL_TYPE','All_Type'),
    ('TREKKING','Trekking'),
    ('HISTORIC','Historic')
)

VEHICLE_TYPE = (
    ('NA','Na'),
    ('MOTOR BIKES','Motor Bike'),
    ('FOUR SEATER','Four Seater'),
    ('FIVE SEATER','Five Seater'),
    ('SIX  SEATER','Six Seater'),
    ('EIGHT SEATER','Four Seater'),
    ('TEN SEATER','Ten Seater')
)
YES_NO_CHOICE = (
    ('YES','Yes'),
    ('NO','No')
)

class GuideUserProfile(models.Model):
    user            = models.OneToOneField(Users, parent_link=True, on_delete=models.CASCADE, related_name='guide_user_profile')
    mobile_number   = models.CharField(_('Phone Number'),max_length=15, blank=False, help_text="Contact Phone Number")
    gender          = models.CharField(max_length=10,
                                       choices=GENDER_CHOICES,
                                       default=GENDER_CHOICES[0][0])
    date_of_birth   = models.DateField()
    nationality     = models.CharField(_('Nationality'), max_length=30, blank=False, null=False)
    profile_pic     = models.ImageField(_('Profile Pic'),upload_to=profile_image_directory_path, blank=True, null=True)
    passport_image  = models.ImageField(_('Passport Image'),upload_to=passport_image_directory_path, blank=True, null=True)
    visa_image      = models.ImageField(_('Visa Image'),upload_to=visa_image_directory_path, blank=True, null=True)

    languages_known         = models.CharField(_('Langauges Knows/Speaks'), max_length=255, blank=False, null=False)
    higher_qualification    = models.CharField(_('Higher Qualification'), max_length=30, blank=False, null=False)
    areas                   = models.CharField(_('Areas Can Guide'), max_length=1000, blank=False,null=False,default='' )
    guide_type              = models.CharField(_('Guide type'), max_length=1000, 
                                                choices=GUIDE_TYPE_CHOICES,
                                                default=GUIDE_TYPE_CHOICES[0][0])
    have_vehicle            = models.CharField(_('Do you have vehicle'),max_length=30, choices=YES_NO_CHOICE,default=YES_NO_CHOICE[1][0])
    vehicle_type            = models.CharField(_('Vehicle Type'), max_length=30,choices=VEHICLE_TYPE,default=VEHICLE_TYPE[0][0])
    gov_id_proof            = models.ImageField(_('Any Goverment ID'), upload_to=gov_id_image_directory_path,
                                                            blank=True, null=True)
    police_verification     = models.ImageField(_('Police Verification Report'), upload_to=police_verification_image_directory_path,
                                                            blank=True, null=True)
    agreement               = models.ImageField(_('Agreement'), upload_to=agreement_image_directory_path,
                                                            blank=True, null=True)
    interview_status        = models.CharField(_('Interview Complete?'), max_length=30, choices=YES_NO_CHOICE,default=YES_NO_CHOICE[0][0])
    rating=models.IntegerField(_('Guide Standard Rating'),blank=True,null=True)
    status=models.BooleanField(_('Availability'),default=True)
    is_featured=models.BooleanField(_('Featured'),default=False)
    is_in_top_ten=models.BooleanField(_('Top Ten'),default=False)
    def __str__(self):
        return self.mobile_number 


class TravelAgencyProfile(models.Model):
    user = models.OneToOneField(Users, parent_link=True, on_delete=models.CASCADE, related_name='agency_user_profile')
    owners_name     = models.CharField(_('Owner Name'), max_length=50, blank=False, null=False, help_text='Owners Name')
    mobile_number   = models.CharField(_('Phone Number'),max_length=15, blank=False, help_text="Contact Phone Number")
    website         = models.CharField(_('Website'), max_length=100, blank=False,null=True)
    address         = models.CharField(_('Address'), max_length=100, blank=False,null=True)
    about           = models.TextField(_('About'), max_length=1000, blank=False,null=True)
    pan             = models.CharField(_('PAN'),max_length=40,blank=True,null=True)
    profile_pic     = models.ImageField(_('Profile Pic'),upload_to=profile_image_directory_path, blank=True, null=True)
    pan_pic         = models.ImageField(_('PAN Image'),upload_to=gov_id_image_directory_path, blank=True, null=True)
    agreement       = models.ImageField(_('Agreement'), upload_to=agreement_image_directory_path,
                                                            blank=True, null=True)
    rating              = models.IntegerField(_('Guide Standard Rating'),blank=True,null=True)
    number_of_employee  = models.IntegerField(_('Number of employee'))
    status              = models.BooleanField(_('Availability'),default=True)
    is_featured         = models.BooleanField(_('Featured'),default=False)
    is_in_top_ten       = models.BooleanField(_('Top Ten'),default=False)

    def __str__(self):
        return self.user.email 


class GuideAgencyReview(models.Model):
    user        = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='guide_agency_review')
    reviewer    = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='guide_agency_reviewer')
    reviews     = models.TextField(_('Reviews'), max_length=1111, blank=True, null=True)
    rating      = models.FloatField(_('Rating'), max_length=5.0, default=1.0, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.place.name)