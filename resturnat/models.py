from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField( max_length=200)
    price=models.models.CharField(max_length=6)
    image=models.ImageField(upload_to='food/')
    description=models.models.TextField(blank=True)