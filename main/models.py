from django.db import models

# Create your models here.


class Location(models.Model):
    # one
    location_name = models.CharField(max_length=200)


class Datapoint(models.Model):
    # many
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    humidity = models.DecimalField(max_digits=3, decimal_places=1)
    temperature_expected = models.IntegerField()
