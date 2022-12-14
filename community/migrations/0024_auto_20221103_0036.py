# Generated by Django 3.2 on 2022-11-02 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0023_auto_20221103_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='Your_Name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='your_email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Last_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
        migrations.AlterField(
            model_name='job_vacancies_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
        migrations.AlterField(
            model_name='videos_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 3, 0, 35, 46, 997689)),
        ),
    ]
