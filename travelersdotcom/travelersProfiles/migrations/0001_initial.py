# Generated by Django 3.1.1 on 2020-11-19 13:40

import core_utility
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuideUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='guide_user_profile', to='travelersUsers.users')),
                ('mobile_number', models.CharField(help_text='Contact Phone Number', max_length=15, verbose_name='Phone Number')),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], default='Male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=30, verbose_name='Nationality')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=core_utility.profile_image_directory_path, verbose_name='Profile Pic')),
                ('passport_image', models.ImageField(blank=True, null=True, upload_to=core_utility.passport_image_directory_path, verbose_name='Passport Image')),
                ('visa_image', models.ImageField(blank=True, null=True, upload_to=core_utility.visa_image_directory_path, verbose_name='Visa Image')),
                ('languages_known', models.CharField(max_length=255, verbose_name='Langauges Knows/Speaks')),
                ('higher_qualification', models.CharField(max_length=30, verbose_name='Higher Qualification')),
                ('areas', models.CharField(default='', max_length=1000, verbose_name='Areas Can Guide')),
                ('guide_type', models.CharField(choices=[('ALL_TYPE', 'All_Type'), ('TREKKING', 'Trekking'), ('HISTORIC', 'Historic')], default='ALL_TYPE', max_length=1000, verbose_name='Guide type')),
                ('have_vehicle', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=30, verbose_name='Do you have vehicle')),
                ('vehicle_type', models.CharField(choices=[('NA', 'Na'), ('MOTOR BIKES', 'Motor Bike'), ('FOUR SEATER', 'Four Seater'), ('FIVE SEATER', 'Five Seater'), ('SIX  SEATER', 'Six Seater'), ('EIGHT SEATER', 'Four Seater'), ('TEN SEATER', 'Ten Seater')], default='NA', max_length=30, verbose_name='Vehicle Type')),
                ('gov_id_proof', models.ImageField(blank=True, null=True, upload_to=core_utility.gov_id_image_directory_path, verbose_name='Any Goverment ID')),
                ('police_verification', models.ImageField(blank=True, null=True, upload_to=core_utility.police_verification_image_directory_path, verbose_name='Police Verification Report')),
                ('agreement', models.ImageField(blank=True, null=True, upload_to=core_utility.agreement_image_directory_path, verbose_name='Agreement')),
                ('interview_status', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=30, verbose_name='Interview Complete?')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Guide Standard Rating')),
                ('status', models.BooleanField(default=True, verbose_name='Availability')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('is_in_top_ten', models.BooleanField(default=False, verbose_name='Top Ten')),
            ],
        ),
    ]
