# Generated by Django 4.2 on 2023-06-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_news_and_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_and_events',
            name='file',
        ),
        migrations.AlterField(
            model_name='upload_images',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='news_and_events',
            name='file',
            field=models.ManyToManyField(blank=True, related_name='events', to='main_app.upload_images'),
        ),
    ]
