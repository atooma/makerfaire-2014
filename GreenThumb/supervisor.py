# -*- coding: utf-8 -*-

import dht11
import time
import os

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
            (humidity, temperature) = ('-', '-')

    print '--------PIN {}----------'.format(pin)
    print 'Humidity: {}%'.format(humidity)
    print 'Temperature: {}°C'.format(temperature)
    print '------------------------'

while True:
    ouput_val(25)
    ouput_val(24)
    ouput_val(18)
    time.sleep(4)
    os.system('clear')