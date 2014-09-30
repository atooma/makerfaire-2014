from flask import Flask, request, jsonify
from config import config
from nanpy import serial_manager, Arduino, Tone
import os
import time
try:
    import boardconfig
except ImportError:
    import boardconfig_sample as boardconfig

app = Flask(__name__)
config_name = (os.getenv('FLASK_CONFIG') or 'default')
app.config.from_object(config[config_name])

@app.route('/move', methods=['POST'])
def move():
    movetype = request.json['type']
    duration = request.json['duration']

    if movetype == 'left':
        Arduino.digitalWrite(boardconfig.motor1_cp1, 0)
        Arduino.digitalWrite(boardconfig.motor1_cp2, 1)
        Arduino.analogWrite(boardconfig.motor1_ep, boardconfig.motor_speed)
    elif movetype == 'right':
        Arduino.digitalWrite(boardconfig.motor1_cp1, 1)
        Arduino.digitalWrite(boardconfig.motor1_cp2, 0)
        Arduino.analogWrite(boardconfig.motor1_ep, boardconfig.motor_speed)
    elif movetype == 'up':
        Arduino.digitalWrite(boardconfig.motor2_cp1, 0)
        Arduino.digitalWrite(boardconfig.motor2_cp2, 1)
        Arduino.analogWrite(boardconfig.motor2_ep, boardconfig.motor_speed)
    elif movetype == 'down':
        Arduino.digitalWrite(boardconfig.motor2_cp1, 1)
        Arduino.digitalWrite(boardconfig.motor2_cp2, 0)
        Arduino.analogWrite(boardconfig.motor2_ep, boardconfig.motor_speed)
    else:
        return jsonify({ 'error' : 'use type up, down, left or right' }), 400
    time.sleep(duration/1000)

    Arduino.analogWrite(boardconfig.motor2_ep, 0)
    Arduino.analogWrite(boardconfig.motor1_ep, 0)

    return jsonify({ 'status' : 'success' }), 200

@app.route('/lights', methods=['POST'])
def lights():
    status = request.json['status']
    if status == 'on':
        Arduino.digitalWrite(boardconfig.lights_pin, 1)
    elif status == 'off':
        Arduino.digitalWrite(boardconfig.lights_pin, 0)
    else:
        return jsonify({ 'error' : 'use status on or off' }), 400
    return jsonify({ 'status' : 'success' }), 200

@app.route('/beep', methods=['POST'])
def beep():
    duration = request.json['duration']
    tone = Tone(boardconfig.beep_pin)
    tone.play(Tone.NOTE_FS1 , duration)
    return jsonify({ 'status' : 'success' }), 200

if __name__ == "__main__":
    serial_manager.timeout = None
    serial_manager.open(boardconfig.serialport)
    Arduino.pinMode(boardconfig.motor1_cp1, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.motor1_cp2, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.motor1_ep, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.motor2_cp1, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.motor2_cp2, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.motor2_ep, Arduino.OUTPUT)
    Arduino.pinMode(boardconfig.lights_pin, Arduino.OUTPUT)
    app.run()