# Generated by Django 5.0.7 on 2024-07-29 14:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_publication_statistic_alter_publication_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 14, 5, 0, 837876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='statistic',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.publicationstatistic'),
        ),
    ]