import chickenfoot
from chickenfoot import app
from flask import url_for
import unittest
import json
from mock import patch

class TestCar(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    @patch('chickenfoot.Arduino.analogWrite')
    @patch('chickenfoot.Arduino.digitalWrite')
    def test_move_ok(self, mock_analogWrite, mock_digitalWrite):
        with app.app_context():
            move_types = ['up', 'down', 'left', 'right']
            move_json = {
                'duration' : 1,
                'type' : 'up'
            }
            for move_type in move_types:
                move_json['type'] = move_type
                response = self.client.post(url_for('move'),
                        data=json.dumps(move_json),
                        content_type='application/json')

                self.assertEqual(response.status_code, 200)

    @patch('chickenfoot.Arduino.analogWrite')
    @patch('chickenfoot.Arduino.digitalWrite')
    def test_move_wrong_par(self, mock_analogWrite, mock_digitalWrite):
        with app.app_context():
            move_json = {
                'duration' : 1,
                'type' : 'burp'
            }
            response = self.client.post(url_for('move'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 400)

            self.assertEqual(mock_digitalWrite.called, False)
            self.assertEqual(mock_analogWrite.called, False)

    @patch('chickenfoot.Arduino.digitalWrite')
    def test_lights_on_ok(self, mock_digitalWrite):
        with app.app_context():
            move_json = {
                'status' : 'on'
            }
            response = self.client.post(url_for('lights'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)
            mock_digitalWrite.assert_called_once_with(chickenfoot.boardconfig.lights_pin, 1)

    @patch('chickenfoot.Arduino.digitalWrite')
    def test_lights_off_ok(self, mock_digitalWrite):
        with app.app_context():
            move_json = {
                'status' : 'off'
            }
            response = self.client.post(url_for('lights'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)
            mock_digitalWrite.assert_called_once_with(chickenfoot.boardconfig.lights_pin, 0)

    @patch('chickenfoot.Arduino.digitalWrite')
    def test_lights_wrong_par(self, mock_digitalWrite):
        with app.app_context():
            move_json = {
                'status' : 'org'
            }
            response = self.client.post(url_for('lights'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 400)
            self.assertEqual(mock_digitalWrite.called, False)

    @patch('chickenfoot.Tone')
    def test_beep_ok(self, tone_mock):
        with app.app_context():
            move_json = {
                'duration' : 1,
            }
            response = self.client.post(url_for('beep'),
                    data=json.dumps(move_json),
                    content_type='application/json')

            self.assertEqual(response.status_code, 200)
            tone_mock.assert_called_once()
