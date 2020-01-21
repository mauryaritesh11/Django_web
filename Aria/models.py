from django.db import models

# Create your models here.

class services(models.Model):
    id= models.IntegerField
    img= models.ImageField(upload_to='pics')
    name= models.CharField(max_length=100)
    intro= models.TextField()
    desc1= models.TextField()
    desc2= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
