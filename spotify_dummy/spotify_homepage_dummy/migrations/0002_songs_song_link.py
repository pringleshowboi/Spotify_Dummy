# Generated by Django 4.2.2 on 2023-08-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_homepage_dummy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_link',
            field=models.URLField(default='https://www.youtube.com/watch?v=-UYgORr5Qhg'),
        ),
    ]