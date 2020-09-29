# Generated by Django 3.1.1 on 2020-09-29 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0003_travelagencyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guideuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='guide_user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='touristuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='tourist_user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='travelagencyprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='agency_user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
