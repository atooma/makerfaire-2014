from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from models import DHTSensor
import json

class SensorTest(TestCase):

    def test_get_correct_values(self):
        DHTSensor.objects.create(id=12, temperature=24, humidity=32)
        response = self.client.get('/api/sensors/dht/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['temperature'], 24)
        self.assertEqual(response.data['results'][0]['humidity'], 32)