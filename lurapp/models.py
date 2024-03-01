from django.db import models

# Create your models here.
class Contact(models.Model):
   Name = models.CharField(max_length=150)
   email = models.CharField(max_length=150)
   phone = models.CharField(max_length=12)
   Message = models.CharField(max_length=10000)