from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    palce = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
