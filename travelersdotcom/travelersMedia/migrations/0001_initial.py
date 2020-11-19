# Generated by Django 3.1.1 on 2020-11-19 13:40

import core_utility
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=555)),
                ('alt', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(default='images/static/defualt.png', upload_to=core_utility.image_directory_path)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default=('active', 'Active'), max_length=15)),
            ],
        ),
    ]
