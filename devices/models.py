from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Document(models.Model):
    url=models.CharField(max_length=255)
    type_url = models.IntegerField()

class Series(models.Model):
    name=models.CharField(max_length=255)
    documents=models.ForeignKey(Document, on_delete=models.CASCADE, default=None)

class Device(models.Model):
    serial_number=models.CharField(max_length=255)
    series=models.OneToOneField(Series)
    date=models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)    
    
class Location(models.Model):
    company=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    devices=models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    
class Files(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
     location = models.OneToOneField(Location, on_delete=models.CASCADE, default=None)
     device = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)

    


    

    

