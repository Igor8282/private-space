from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    name=models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    organization = models.CharField(max_length=255)
    applications=models.ManyToManyField(Application)
    
class Notification(models.Model):
    user = models.OneToOneField(User)
    status=models.IntegerField()
    application=models.ForeignKey(Application)
    
