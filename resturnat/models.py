from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField( max_length=200)
    price=models.CharField(max_length=6)
    image=models.ImageField(upload_to='food')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


    
    
class Quotes(models.Model):
    name=models.CharField(max_length=50)
    quote=models.TextField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name    

class Appointment(models.Model):
    name=models.CharField( max_length=200)
    email=models.EmailField(blank=True)
    phone=models.CharField( max_length=15)
    message=models.TextField(blank=True)
    number_of_guests=models.CharField( max_length=4)
    date=models.DateTimeField( blank=True,null=True,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    

class Qoute(models.Model):
    name=models.CharField(max_length=50)
    quote=models.TextField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name    
    