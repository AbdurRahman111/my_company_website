# Generated by Django 3.2 on 2022-11-01 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_auto_20221101_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation_table',
            options={'verbose_name_plural': 'Organisation Table'},
        ),
        migrations.AddField(
            model_name='organisation_table',
            name='slug',
            field=models.SlugField(default='Auto-Generate', editable=False),
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 16, 41, 17, 406284)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 16, 41, 17, 406284)),
        ),
        migrations.AlterField(
            model_name='organisation_table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='organisation_img/'),
        ),
    ]
