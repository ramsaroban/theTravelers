
def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/images/{0}'.format(filename)

def profile_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/profiles/{0}'.format(filename)

def passport_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/passport/{0}'.format(filename)

def visa_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/visa/{0}'.format(filename)

def gov_id_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/partners/gov_id/{0}'.format(filename)


def police_verification_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/partners/gov_id/{0}'.format(filename)


def agreement_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist_name/<filename>
    return 'Images/partners/agreement/{0}'.format(filename)





from django.utils.text import slugify
 
def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__
 
    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1
 
    return unique_slug