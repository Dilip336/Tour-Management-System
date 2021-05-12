from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator


# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    title = models.CharField(max_length=50)
    content = models.TextField(validators=[MaxLengthValidator(220)])
    
    def __str__(self):
        return self.title 

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

class Booking(models.Model):
    
     travellingform = models.CharField(max_length=20)
     travellingto =  models.CharField(max_length=20)
     Departing = models.DateTimeField()
     Returing = models.DateTimeField()
     Adults = models.IntegerField()
     Childern = models.IntegerField()
    #  Travel_Types= (
    #      ('Bus','Bus')
    #      ('Aeo','Aeroplane')
       

    #  )
     def __str__(self):
        return self.name
    



    
   
