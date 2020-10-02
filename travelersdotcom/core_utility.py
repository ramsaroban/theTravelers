
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
