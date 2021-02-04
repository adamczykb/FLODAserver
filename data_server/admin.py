from django.contrib import admin
from .models import TypeOfLightning, LightningDetail, TemperatureDetail, HumidityDetail, WateringDetail, \
    DeclaredSpecies, Devices, States, UserConfigurations


# Register your models here.
@admin.register(TypeOfLightning)
@admin.register(LightningDetail)
@admin.register(TemperatureDetail)
@admin.register(HumidityDetail)
@admin.register(WateringDetail)
@admin.register(DeclaredSpecies)
@admin.register(Devices)
@admin.register(States)
@admin.register(UserConfigurations)
class Floda(admin.ModelAdmin):
    list_display = ()
