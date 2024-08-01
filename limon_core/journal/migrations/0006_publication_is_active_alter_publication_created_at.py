# Generated by Django 5.0.7 on 2024-07-31 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_publication_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 12, 19, 3, 553623, tzinfo=datetime.timezone.utc)),
        ),
    ]
