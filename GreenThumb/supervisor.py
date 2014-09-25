# -*- coding: utf-8 -*-

import dht11
import time
import os
import requests
import json

measurements_buffer = {}

def ouput_val(pin):
    pin_hash = str(pin)
    try:
        (humidity, temperature) = dht11.read(pin)
        measurements_buffer[pin_hash] = (humidity, temperature)
    except:
        if pin_hash in measurements_buffer:
            (humidity, temperature) = measurements_buffer[pin_hash]
        else:
            (humidity, temperature) = (-1, -1)
            return

    print '--------PIN {}----------'.format(pin)
    print 'Humidity: {}%'.format(humidity)
    print 'Temperature: {}°C'.format(temperature)
    print '------------------------'
    data = {'id':pin, 'temperature': temperature, 'humidity': humidity}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    requests.put('http://localhost:9092/api/sensors/dht/{}/'.format(pin),
        data=json.dumps(data), headers=headers, auth=('andrea', 'andrea'))


while True:
    ouput_val(25)
    ouput_val(24)
    ouput_val(18)
    time.sleep(4)
    os.system('clear')