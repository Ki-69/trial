# Generated by Django 4.2 on 2023-06-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_alter_admissions_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissions',
            name='file',
            field=models.FileField(default=None, upload_to='website/files'),
        ),
    ]
