# Generated by Django 5.0.7 on 2024-07-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, null=True)),
                ('short_description', models.TextField(max_length=500, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('date', models.DateTimeField(null=True)),
                ('reading_time', models.IntegerField(default=0)),
            ],
        ),
    ]
