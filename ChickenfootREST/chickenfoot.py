from flask import Flask, request, jsonify
from config import config
from nanpy import serial_manager, Arduino, Tone
import os
import time

app = Flask(__name__)
config_name = (os.getenv('FLASK_CONFIG') or 'default')
app.config.from_object(config[config_name])

motor1_cp1 = 4
motor1_cp2 = 5
motor1_ep = 10
motor2_cp1 = 2
motor2_cp2 = 3
motor2_ep = 9
motor_speed = 1000
lights_pin = 13
beep_pin = 8

@app.route('/move', methods=['POST'])
def move():
    movetype = request.json['type']
    duration = request.json['duration']

    if movetype == 'left':
        Arduino.digitalWrite(motor1_cp1, 0)
        Arduino.digitalWrite(motor1_cp2, 1)
        Arduino.analogWrite(motor1_ep, motor_speed)
    elif movetype == 'right':
        Arduino.digitalWrite(motor1_cp1, 1)
        Arduino.digitalWrite(motor1_cp2, 0)
        Arduino.analogWrite(motor1_ep, motor_speed)
    elif movetype == 'up':
        Arduino.digitalWrite(motor2_cp1, 0)
        Arduino.digitalWrite(motor2_cp2, 1)
        Arduino.analogWrite(motor2_ep, motor_speed)
    elif movetype == 'down':
        Arduino.digitalWrite(motor2_cp1, 1)
        Arduino.digitalWrite(motor2_cp2, 0)
        Arduino.analogWrite(motor2_ep, motor_speed)
    else:
        return jsonify({ 'error' : 'use type up, down, left or right' }), 400
    time.sleep(duration/1000)

    Arduino.digitalWrite(motor2_cp1, 0)
    Arduino.digitalWrite(motor2_cp2, 0)
    Arduino.analogWrite(motor2_ep, 0)

    Arduino.digitalWrite(motor1_cp1, 0)
    Arduino.digitalWrite(motor1_cp2, 0)
    Arduino.analogWrite(motor1_ep, 0)

    return jsonify({ 'status' : 'success' }), 200

@app.route('/lights', methods=['POST'])
def lights():
    status = request.json['status']
    if status == 'on':
        Arduino.digitalWrite(lights_pin, 1)
    elif status == 'off':
        Arduino.digitalWrite(lights_pin, 0)
    else:
        return jsonify({ 'error' : 'use status on or off' }), 400
    return jsonify({ 'status' : 'success' }), 200

@app.route('/beep', methods=['POST'])
def beep():
    duration = request.json['duration']
    tone = Tone(beep_pin)
    tone.play(Tone.NOTE_FS1 , duration)
    return jsonify({ 'status' : 'success' }), 200

if __name__ == "__main__":
    serial_manager.timeout = None
    serial_manager.open('/dev/tty.usbmodem14121')
    Arduino.pinMode(motor1_cp1, Arduino.OUTPUT)
    Arduino.pinMode(motor1_cp2, Arduino.OUTPUT)
    Arduino.pinMode(motor1_ep, Arduino.OUTPUT)
    Arduino.pinMode(motor2_cp1, Arduino.OUTPUT)
    Arduino.pinMode(motor2_cp2, Arduino.OUTPUT)
    Arduino.pinMode(motor2_ep, Arduino.OUTPUT)
    Arduino.pinMode(lights_pin, Arduino.OUTPUT)
    app.run()