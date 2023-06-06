# Generated by Django 4.2 on 2023-06-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='news_and_events',
            name='file',
        ),
        migrations.AddField(
            model_name='news_and_events',
            name='file',
            field=models.ManyToManyField(blank=True, related_name='watch_listings', to='main_app.upload_images'),
        ),
    ]
