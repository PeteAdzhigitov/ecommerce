from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY = (('',''),)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Items(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/static_dirs/items_images/')
    description = models.CharField(max_length=255)
    price = models.FloatField()
    category = 
