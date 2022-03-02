from django.db import models

# Create your models here.


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Field(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    location = models.CharField(max_length=100)


class Vehicle(models.Model):
    name = models.CharField(max_length=50)


class Machine(models.Model):
    name = models.CharField(max_length=50)


class VehicleType(models.Model):
    name = models.CharField(max_length=50)
