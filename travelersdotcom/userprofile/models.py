from django.db import models
import uuid
from django.conf import settings
from phone_field import PhoneField
from django.utils.translation import ugettext_lazy as _ 

# Create your models here.
#Gender Choices 
GENDER_CHOICES = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Others','OTHERS')
)
# Model for User Account
class TouristUserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, parent_link=True, on_delete=models.CASCADE, related_name='tourist_user_profile')
    mobile_number   = PhoneField(blank=False, help_text="Contact Phone Number")
    gender          = models.CharField(max_length=10,
                                       choices=GENDER_CHOICES,
                                       default=GENDER_CHOICES[0][0])
    date_of_birth   = models.DateField()
    nationality     = models.CharField(_('Nationality'), max_length=30, blank=False, null=False)
    profile_pic     = models.ImageField(upload_to='tourist/profile/', blank=False, null=False)
    passport_image  = models.ImageField(upload_to='tourist/passport/', blank=True, null=True)
    visa_image      = models.ImageField(upload_to='tourist/visa/', blank=True, null=True)


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, parent_link=True, on_delete=models.CASCADE, related_name='guide_user_profile')

    mobile_number   = PhoneField(blank=False, help_text="Contact Phone Number")
    gender          = models.CharField(max_length=10,
                                       choices=GENDER_CHOICES,
                                       default=GENDER_CHOICES[0][0])
    date_of_birth   = models.DateField()
    nationality     = models.CharField(_('Nationality'), max_length=30, blank=False, null=False)
    profile_pic     = models.ImageField(upload_to='guide/profile/', blank=False, null=False, default='')
    
    passport_image  = models.ImageField(upload_to='guide/passport/', blank=False, null=False, default='')
    visa_image      = models.ImageField(upload_to='guide/visa/', blank=True, null=True, default='')
    languages_known         = models.CharField(_('Langauges Knows/Speaks'), max_length=255, blank=False, null=False)
    higher_qualification    = models.CharField(_('Higher Qualification'), max_length=30, blank=False, null=False)
    areas                   = models.CharField(_('Areas Can Guide'), max_length=1000, blank=False,null=False,default='' )
    guide_type              = models.CharField(_('Guide type'), max_length=1000, 
                                                choices=GUIDE_TYPE_CHOICES,
                                                default=GUIDE_TYPE_CHOICES[0][0])
    have_vehicle            = models.CharField(_('Do you have vehicle'),max_length=30, choices=YES_NO_CHOICE,default=YES_NO_CHOICE[0][0])
    vehicle_type            = models.CharField(_('Vehicle Type'), max_length=30,choices=VEHICLE_TYPE,default=VEHICLE_TYPE[0][0])
    gov_id_proof            = models.ImageField(_('Any Goverment ID'), upload_to='guide/gov_id/',
                                                            blank=False, null=False, default='')
    police_verification     = models.ImageField(_('Police Verification Report'), upload_to='guide/police_verification/',
                                                            blank=False, null=False, default='')
    agreement               = models.ImageField(_('Agreement'), upload_to='guide/agreement/',
                                                            blank=False, null=False, default='')
    interview_status        = models.CharField(_('Interview Complete?'), max_length=30, choices=YES_NO_CHOICE,default=YES_NO_CHOICE[0][0])
    rating=models.IntegerField(_('Guide Standard Rating'),blank=True,null=True)
    status=models.BooleanField(_('Availability'),default=True)
    def __str__(self):
        return self.user.email 


class TravelAgencyProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, parent_link=True, on_delete=models.CASCADE, related_name='agency_user_profile')
    mobile_number   = PhoneField(blank=False, help_text="Contact Phone Number")
    website         = models.CharField(_('Website'), max_length=100, blank=False,null=True)
    address         = models.CharField(_('Address'), max_length=100, blank=False,null=True)
    bio             = models.TextField(_('BIO'), max_length=1000, blank=False,null=True)
    pan             =models.CharField(_('PAN'),max_length=40,blank=True,null=True)
    profile_pic     = models.ImageField(upload_to='agency/profile/', blank=False, null=False, default='')
    agreement       = models.ImageField(_('Agreement'), upload_to='guide/agreement/',
                                                            blank=False, null=False, default='')
    rating          =models.IntegerField(_('Guide Standard Rating'),blank=True,null=True)
    number_of_employee=models.IntegerField(_('Number of employee'))
    status=models.BooleanField(_('Availability'),default=True)
    is_featured=models.BooleanField(_('Featured'),default=False)
    is_in_top_ten=models.BooleanField(_('Top Ten'),default=False)

    def __str__(self):
        return self.user.email 