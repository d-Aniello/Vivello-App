from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    """user = models.OneToOneField(User, on_delete=models.CASCADE)"""
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

    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse('vehicle_type_delete_view', args=(self.pk, ))


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.vehicle_type}"

    def get_absolute_url(self):
        return reverse('vehicle_detail_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('vehicle_delete_view', args=(self.pk, ))


class MachineType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    def get_delete_url(self):
        return reverse('machine_type_delete_view', args=(self.pk, ))


class Machine(models.Model):
    name = models.CharField(max_length=50)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.machine_type}"

    def get_absolute_url(self):
        return reverse('machine_detail_view', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('machine_delete_view', args=(self.pk, ))


class Crop(models.Model):
    name = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.variety}"

    def get_delete_url(self):
        return reverse('crop_delete_view', args=(self.pk, ))


class Task(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    date = models.DateField()
    """user = models.OneToOneField(User, on_delete=models.CASCADE)"""
    vehicle = models.ManyToManyField(Vehicle)
    machine = models.ManyToManyField(Machine)
    field = models.ManyToManyField(Field)
    crop = models.ManyToManyField(Crop, blank=True)
