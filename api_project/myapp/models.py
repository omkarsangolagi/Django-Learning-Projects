from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    email = models.EmailField()
    place = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    salary = models.IntegerField()
