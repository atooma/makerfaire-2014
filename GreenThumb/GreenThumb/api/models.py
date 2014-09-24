from django.db import models

class DHTSensor(models.Model):
    id = models.IntegerField(primary_key=True)
    humidity = models.IntegerField()
    temperature = models.IntegerField()