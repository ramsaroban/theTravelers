# Generated by Django 3.1.1 on 2020-09-22 01:17

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristUserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='tourist_user_profile', to='travelersUsers.users')),
                ('mobile_number', phone_field.models.PhoneField(help_text='Contact Phone Number', max_length=31)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], default='Male', max_length=10)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=30, verbose_name='Nationality')),
                ('profile_pic', models.ImageField(upload_to='profile/')),
                ('passport_image', models.ImageField(blank=True, null=True, upload_to='passport/')),
                ('visa_image', models.ImageField(blank=True, null=True, upload_to='visa/')),
            ],
        ),
    ]
