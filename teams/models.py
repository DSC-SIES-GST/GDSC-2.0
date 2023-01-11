from django.db import models
from datetime import datetime

# Create your models here.

class Domain(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/domain/')
    is_active = models.BooleanField(default=False)
    # slug = models.CharField(max_length=200,blank=False,null=False)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title   
    



class Member(models.Model):
    title = models.ForeignKey(Domain, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,blank=False,null=False)
    photo = models.ImageField(upload_to='photos/domain/members/')
    is_lead = models.BooleanField(default=False)
    is_colead = models.BooleanField(default=False)
    is_coord = models.BooleanField(default=True)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    mail_id = models.EmailField()
    github = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now) 

    def __str__(self):
        return self.name    