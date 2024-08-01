# Generated by Django 5.0.7 on 2024-07-29 14:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_aboutme_category_hashtag_publicationstatistic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='statistic',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.publicationstatistic'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 14, 4, 35, 286415, tzinfo=datetime.timezone.utc)),
        ),
    ]
