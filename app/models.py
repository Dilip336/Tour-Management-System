from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.db.models.fields import CharField


# Create your models here.
class Booking(models.Model):
    
     travellingform = models.CharField(max_length=20,null=True)
     travellingto =  models.CharField(max_length=20,null=True)
     departing = models.DateTimeField(null=True)
     returing = models.DateTimeField(null=True)
     adults = models.IntegerField(null=True)
     childern = models.IntegerField(null=True)
     traveltypes = models.CharField(max_length=50,null=True)


class Search(models.Model):

     title = models.CharField(max_length=100,null=True)
     image = models.CharField(max_length=100,null=True)
     description = models.CharField(max_length=1000,null=True)
     upperclass = models.CharField(max_length=100,null=True)
     lowerclass = models.CharField(max_length=100,null=True)
