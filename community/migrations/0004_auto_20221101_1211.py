# Generated by Django 3.2 on 2022-11-01 06:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0003_auto_20221101_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 12, 11, 38, 416758)),
        ),
        migrations.CreateModel(
            name='news_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 12, 11, 38, 417755))),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.news_table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
