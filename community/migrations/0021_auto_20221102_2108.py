# Generated by Django 3.2 on 2022-11-02 15:08

import datetime
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0020_auto_20221102_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Last_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='post_youtube_video',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 2, 21, 8, 18, 917819)),
        ),
        migrations.AlterField(
            model_name='post_youtube_video',
            name='video_url_link',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
