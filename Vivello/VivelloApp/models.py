from django.db import models

# Create your models here.
from django.urls import reverse


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    vehicle = models.ManyToManyField('Vehicle', blank=True)
    machine = models.ManyToManyField('Machine', blank=True)

    def __str__(self):
        return f"{self.name}, {self.address}"

    def get_absolute_url(self):
        return reverse('farm_detail_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('farm_delete_view', args=(self.pk, ))


class Field(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    location = models.CharField(max_length=100)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop = models.ManyToManyField('Crop', blank=True)

    def __str__(self):
        return f"{self.name}, {self.location}"

    def get_absolute_url(self):
        return reverse('field_detail_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('field_delete_view', args=(self.pk, ))


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
