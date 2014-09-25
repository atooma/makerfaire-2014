from models import DHTSensor
from rest_framework import serializers

class DHTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHTSensor
        fields = ('id', 'temperature', 'humidity')
