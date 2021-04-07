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

    def __str__(self):
        return self.name
    



    
   
