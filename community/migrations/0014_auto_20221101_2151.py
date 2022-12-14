# Generated by Django 3.2 on 2022-11-01 15:51

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_auto_20221101_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='Auto-Generate', editable=False)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='events/')),
                ('Details', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects Table',
            },
        ),
        migrations.AlterField(
            model_name='news_comments',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 21, 51, 56, 241120)),
        ),
        migrations.AlterField(
            model_name='news_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 1, 21, 51, 56, 240123)),
        ),
    ]
