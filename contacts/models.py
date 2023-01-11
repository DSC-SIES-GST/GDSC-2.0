from django.db import models
from datetime import datetime
# Create your models here.

class Faq(models.Model):
    question = models.CharField(max_length=200, blank=False)
    answer = models.TextField(blank=False)
    is_live = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.question