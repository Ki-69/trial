# Generated by Django 4.2 on 2023-06-07 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_gallery_alter_images_event_images_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
    ]
