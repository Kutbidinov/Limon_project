from django.db import models

class Publication(models.Model):
    topic = models.CharField(max_length=255, null=True)
    short_description = models.TextField(max_length=500, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    date = models.DateTimeField(null=True)
    reading_time = models.IntegerField(default=0)
