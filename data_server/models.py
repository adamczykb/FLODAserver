from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TypeOfLightning(models.Model):
    name = models.CharField(max_length=255)
    fro = models.FloatField()
    to = models.FloatField()
    pictogram = models.ImageField()


class LightningDetail(models.Model):
    typeof = models.ForeignKey(to=TypeOfLightning, on_delete=models.DO_NOTHING)
    active = models.BooleanField(verbose_name="Sprawdzać ten parametr?")


class TemperatureDetail(models.Model):
    fro = models.FloatField()
    to = models.FloatField()
    active = models.BooleanField(verbose_name="Sprawdzać ten parametr?")


class HumidityDetail(models.Model):
    fro = models.FloatField()
    to = models.FloatField()
    active = models.BooleanField(verbose_name="Sprawdzać ten parametr?")


class WateringDetail(models.Model):
    name = models.CharField(max_length=255)
    howMany = models.IntegerField(verbose_name="Co ile dni podlewać?")
    minHumidity = models.FloatField(verbose_name="Minimalna wilgotność gleby", default=0)
    active = models.BooleanField(verbose_name="Sprawdzać ten parametr?")


class DeclaredSpecies(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    display = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    light = models.ForeignKey(to=LightningDetail, on_delete=models.CASCADE)
    temperature = models.ForeignKey(to=TemperatureDetail, on_delete=models.CASCADE)
    humidity = models.ForeignKey(to=HumidityDetail, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)


class Devices(models.Model):
    added = models.DateTimeField(auto_now=True)
    SDID = models.CharField(max_length=50, verbose_name="Numer idenrtfikacyjny urządzenia")


class States(models.Model):
    device_id = models.ForeignKey(to=Devices, on_delete=models.DO_NOTHING)
    species = models.ForeignKey(to=DeclaredSpecies, on_delete=models.DO_NOTHING)
    watering = models.BooleanField(default=True)
    humidity = models.BooleanField(default=True)
    temperature = models.BooleanField(default=True)
    lightning = models.BooleanField(default=True)


class UserConfigurations(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    device_id = models.ForeignKey(to=Devices, on_delete=models.DO_NOTHING)
    species = models.ForeignKey(to=DeclaredSpecies, on_delete=models.DO_NOTHING)
    overview = models.ForeignKey(to=States, on_delete=models.DO_NOTHING)
