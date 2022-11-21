# Generated by Django 3.2 on 2022-11-01 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_auto_20221101_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events_table',
            options={'verbose_name_plural': 'Event Table'},
        ),
        migrations.AddField(
            model_name='events_table',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 18, 43, 33, 440081)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 18, 43, 33, 440081)),
        ),
    ]