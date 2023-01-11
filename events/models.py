from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/events/%Y/%m/%d/')
    description = models.TextField(blank=True)
    linktext = models.CharField(max_length=200)
    is_live = models.BooleanField(default=False)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title