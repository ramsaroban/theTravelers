# Generated by Django 3.1.1 on 2020-10-01 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelersProfiles', '0007_touristuserprofile_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristuserprofile',
            name='photos',
        ),
    ]
