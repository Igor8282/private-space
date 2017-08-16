from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Document(models.Model):
    url=models.CharField(max_length=255)
    type_url= models.IntegerField(max_length=2)

class Series(models.Model):
    name=models.CharField(max_length=255)
    documents=models.ForeignKey(Document, on_delete=models.CASCADE, default=None)

class Device (models.Model):
    serial_number=models.CharField(max_length=255)
    series=models.ForeignKey(Series, on_delete=models.CASCADE, default=None)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=255)    
    
class Location(models.Model):
    company=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    devices=models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    
class Files(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
     locations=models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
     devices=models.ForeignKey(Device, on_delete=models.CASCADE, default=None)

    


    

    

