from datetime import datetime

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_measure = models.DateTimeField(auto_now_add=datetime.utcnow)
