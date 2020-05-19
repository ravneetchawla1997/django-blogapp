from django.db import models
from datetime import datetime

# Create your models here.
class upload(models.Model):
    Title=models.CharField(max_length=30,default='')
    Description=models.CharField(max_length=500,default='')
    name=models.CharField(max_length=50)
    pic=models.FileField(upload_to='image/')
    author=models.CharField(max_length=50)
    upload_date=models.DateTimeField(default=datetime.now)
