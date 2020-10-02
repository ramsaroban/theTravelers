# Generated by Django 3.1.1 on 2020-09-30 09:49

import core_utility
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelersProfiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristuserprofile',
            name='photos',
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='passport_image',
            field=models.ImageField(blank=True, null=True, upload_to=core_utility.passport_image_directory_path, verbose_name='Passpoer Image'),
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='profile_pic',
            field=models.ImageField(upload_to=core_utility.profile_image_directory_path, verbose_name='Profile Pic'),
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='visa_image',
            field=models.ImageField(blank=True, null=True, upload_to=core_utility.visa_image_directory_path, verbose_name='Visa Image'),
        ),
    ]
