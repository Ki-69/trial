# Generated by Django 4.2 on 2023-05-25 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_member_list_vacancy_vmc_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VMC_members',
            new_name='vmc_member',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacant_deignation',
            new_name='vacant_designation',
        ),
    ]
