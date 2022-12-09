from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    geo_location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)