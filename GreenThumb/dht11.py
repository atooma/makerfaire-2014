import RPi.GPIO as GPIO
import time

class DHT11Exception(Exception):
    pass

def read(pin):
    def bin2dec(string_num):
        return str(int(string_num, 2))

    data = []

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.02)

    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for i in range(0,500):
        data.append(GPIO.input(pin))

    bit_count = 0
    tmp = 0
    count = 0
    humidity_bit = ''
    temperature_bit = ''
    crc = ''

    try:
        while data[count] == 1:
            tmp = 1
            count = count + 1

        for i in range(0, 32):
            bit_count = 0

            while data[count] == 0:
                tmp = 1
                count = count + 1

            while data[count] == 1:
                bit_count = bit_count + 1
                count = count + 1

            if bit_count > 3:
                if i>=0 and i<8:
                    humidity_bit = humidity_bit + '1'
                if i>=16 and i<24:
                    temperature_bit = temperature_bit + '1'
            else:
                if i>=0 and i<8:
                    humidity_bit = humidity_bit + '0'
                if i>=16 and i<24:
                    temperature_bit = temperature_bit + '0'

    except:
        raise DHT11Exception('Error Range')

    try:
        for i in range(0, 8):
            bit_count = 0

            while data[count] == 0:
                tmp = 1
                count = count + 1

            while data[count] == 1:
                bit_count = bit_count + 1
                count = count + 1

            if bit_count > 3:
                crc = crc + '1'
            else:
                crc = crc + '0'
    except:
        raise DHT11Exception('Error Range')

    humidity = bin2dec(humidity_bit)
    temperature = bin2dec(temperature_bit)

    if int(humidity) + int(temperature) - int(bin2dec(crc)) == 0:
        return (humidity, temperature)
    else:
        raise DHT11Exception('Error CRC')