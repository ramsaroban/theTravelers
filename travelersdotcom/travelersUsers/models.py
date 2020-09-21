from django.db import models
from django.utils.translation import ugettext_lazy as _ 
import uuid
from django.conf import settings
from phone_field import PhoneField

from django.contrib.auth.models import ( 
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, middle_name = None, password = None, user_type=None):

        if not email:
            raise ValueError(_('User must have an email address'))

        if not first_name:
            raise ValueError(_('Users must have first'))

        if not last_name:
            raise ValueError(_('User must have last name'))
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
        )

        if user_type:
            user.user_type = user_type

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, first_name=None, last_name=None, middle_name=None):
        
        if not password:
            raise ValueError(_('User must have password'))
        first_name = 'super'
        last_name = 'user'

        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            middle_name = middle_name,
            password=password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class Users(AbstractBaseUser, PermissionsMixin):

    class Types(models.TextChoices):
        TOURIST = 'Tourist','TOURIST'
        GUIDE = 'Guide','GUIDE'
        TRAVEL_AGENCY = 'Travel Agency', 'TRAVEL AGENCY'
    
    user_type       = models.CharField(_('User Type'), max_length=50, choices=Types.choices, default=Types.TOURIST)
    email      = models.EmailField(_('Email Address'), max_length=255, unique=True, db_index=True)
    first_name      = models.CharField(_('first name'), max_length =30,blank=False,null=False)
    middle_name     = models.CharField(_('middle name'), max_length=30,blank=True, null=True, default='')
    last_name       = models.CharField(_('last name'), max_length=30,blank=False, null=False)
    is_verified     = models.BooleanField(_('Is Verified'), default=False)
    is_active       = models.BooleanField(_('is Active'), default=True)
    is_staff        = models.BooleanField(_('is Staff'), default=False)
    is_admin        = models.BooleanField(_('is Admin'), default=False)
    is_superuser    = models.BooleanField(_('is Super User'), default=False)

    created_at      = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(_('last login'), auto_now=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FILED  =   ['first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''


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
    profile_pic     = models.ImageField(upload_to='profile/', blank=False, null=False)
    passport_image  = models.ImageField(upload_to='passport/', blank=True, null=True)
    visa_image      = models.ImageField(upload_to='visa/', blank=True, null=True)


    def __str__(self):
        return self.user.email 