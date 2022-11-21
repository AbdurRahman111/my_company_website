# Generated by Django 3.2 on 2022-11-02 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0019_auto_20221102_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post_youtube_video',
            options={'verbose_name_plural': 'Post Youtube Video'},
        ),
        migrations.RenameField(
            model_name='post_youtube_video',
            old_name='youtube_url_link',
            new_name='video_url_link',
        ),
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Last_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
        migrations.AlterField(
            model_name='post_youtube_video',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 7, 43, 312751)),
        ),
    ]