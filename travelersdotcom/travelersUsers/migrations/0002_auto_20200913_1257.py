# Generated by Django 3.1.1 on 2020-09-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelersUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is Active'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='is Admin'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='is Staff'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='is Super User'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Is Verified'),
        ),
    ]