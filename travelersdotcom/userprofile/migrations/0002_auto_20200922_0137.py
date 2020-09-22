# Generated by Django 3.1.1 on 2020-09-22 01:37

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideUserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='guide_user_profile', to='travelersUsers.users')),
                ('mobile_number', phone_field.models.PhoneField(help_text='Contact Phone Number', max_length=31)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], default='Male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=30, verbose_name='Nationality')),
                ('profile_pic', models.ImageField(default='', upload_to='guide/profile/')),
                ('passport_image', models.ImageField(default='', upload_to='guide/passport/')),
                ('visa_image', models.ImageField(blank=True, default='', null=True, upload_to='guide/visa/')),
                ('languages_known', models.CharField(max_length=255, verbose_name='Langauges Knows/Speaks')),
                ('higher_qualification', models.CharField(max_length=30, verbose_name='Higher Qualification')),
                ('areas', models.CharField(default='', max_length=1000, verbose_name='Areas Can Guide')),
                ('guide_type', models.CharField(choices=[('ALL_TYPE', 'All_Type'), ('TREKKING', 'Trekking'), ('HISTORIC', 'Historic')], default='ALL_TYPE', max_length=1000, verbose_name='Guide type')),
                ('have_vehicle', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=30, verbose_name='Do you have vehicle')),
                ('vehicle_type', models.CharField(choices=[('NA', 'Na'), ('MOTOR BIKES', 'Motor Bike'), ('FOUR SEATER', 'Four Seater'), ('FIVE SEATER', 'Five Seater'), ('SIX  SEATER', 'Six Seater'), ('EIGHT SEATER', 'Four Seater'), ('TEN SEATER', 'Ten Seater')], default='NA', max_length=30, verbose_name='Vehicle Type')),
                ('gov_id_proof', models.ImageField(default='', upload_to='guide/gov_id/', verbose_name='Any Goverment ID')),
                ('police_verification', models.ImageField(default='', upload_to='guide/police_verification/', verbose_name='Police Verification Report')),
                ('agreement', models.ImageField(default='', upload_to='guide/agreement/', verbose_name='Agreement')),
                ('interview_status', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=30, verbose_name='Interview Complete?')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Guide Standard Rating')),
                ('status', models.BooleanField(default=True, verbose_name='Availability')),
            ],
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='passport_image',
            field=models.ImageField(blank=True, null=True, upload_to='tourist/passport/'),
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='tourist/profile/'),
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='visa_image',
            field=models.ImageField(blank=True, null=True, upload_to='tourist/visa/'),
        ),
    ]
