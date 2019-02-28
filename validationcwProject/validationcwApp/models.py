from django.db import models

# Create your models here.
class newCarModel(models.Model):
    make = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=200, default='')
    year = models.IntegerField(max_length=200, default='')
    mpg = models.IntegerField(max_length=200, default='')
