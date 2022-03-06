from django.db import models

# Create your models here.


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Field(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    location = models.CharField(max_length=100)


class VehicleType(models.Model):
    name = models.CharField(max_length=50)


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)


class MachineType(models.Model):
    name = models.CharField(max_length=50)


class Machine(models.Model):
    name = models.CharField(max_length=50)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)


class Crop(models.Model):
    name = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
