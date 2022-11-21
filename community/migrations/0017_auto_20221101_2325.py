# Generated by Django 3.2 on 2022-11-01 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_auto_20221101_2317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_vacancies_table',
            options={'verbose_name_plural': 'Job Vacancies Table'},
        ),
        migrations.RenameField(
            model_name='job_vacancies_table',
            old_name='Short_Description',
            new_name='Description',
        ),
        migrations.RemoveField(
            model_name='job_vacancies_table',
            name='file',
        ),
        migrations.AddField(
            model_name='job_vacancies_table',
            name='Last_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 1, 23, 25, 10, 559920)),
        ),
        migrations.AddField(
            model_name='job_vacancies_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 23, 25, 10, 559920)),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 23, 25, 10, 559920)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 23, 25, 10, 559920)),
        ),
    ]
