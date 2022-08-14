#from typing_extensions import Self
from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=70)
   email = models.CharField(max_length=70)
   phone = models.CharField(max_length=12)
   desc = models.TextField()

   def __str__(self):
       return self.name
   
   
     
