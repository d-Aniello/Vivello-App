from django.db import models

# Create your models here.


class Field(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    location = models.CharField(max_length=100)