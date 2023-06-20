# Generated by Django 4.2 on 2023-06-06 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_delete_news_and_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_and_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('file', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='main_app.upload_images')),
            ],
        ),
    ]