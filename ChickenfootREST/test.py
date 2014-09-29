from chickenfoot import app
from flask import url_for
import unittest
import json

class TestCar(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_move_ok(self):
        with app.app_context():
            move_json = {
                'duration' : 1000,
                'type' : 'up'
            }
            response = self.client.post(url_for('move'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)

    def test_lights_ok(self):
        with app.app_context():
            move_json = {
                'status' : 'on'
            }
            response = self.client.post(url_for('lights'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)

    def test_beep_ok(self):
        with app.app_context():
            move_json = {
                'duration' : 1000,
            }
            response = self.client.post(url_for('beep'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)