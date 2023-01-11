from django.db import models
from datetime import datetime


# Create your models here.

class Sessions(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    is_live = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)


class Faq(models.Model):
    question = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_live = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)
