from django.core.urlresolvers import resolve
import base64
from django.test import TestCase
from django.http import HttpRequest
from rest_framework.test import APIClient
from models import DHTSensor
from django.contrib.auth.models import User
import json

class SensorTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('testuser',
                                             'testuser@news.com', 'testuserpsw')

    def test_get_all_sensor_correct_values(self):
        DHTSensor.objects.create(id=12, temperature=24, humidity=32)
        response = self.client.get('/api/sensors/dht/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['temperature'], 24)
        self.assertEqual(response.data['results'][0]['humidity'], 32)

    def test_get_single_sensor_correct_values(self):
        DHTSensor.objects.create(id=12, temperature=24, humidity=32)
        response = self.client.get('/api/sensors/dht/{}/'.format(12))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['temperature'], 24)
        self.assertEqual(response.data['humidity'], 32)

    def test_post_single_sensor_values(self):
        credentials = base64.b64encode('testuser:testuserpsw')
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Basic ' + credentials
        response = self.client.post('/api/sensors/dht/',
            {'id' : 12, 'temperature' : 24, 'humidity' : 32})
        self.assertEqual(response.status_code, 201)