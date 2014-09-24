from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import DHTSerializer
from models import DHTSensor


class DHTSensorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DHT sensors values to be viewed or edited.
    """
    queryset = DHTSensor.objects.all()
    serializer_class = DHTSerializer