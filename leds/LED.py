import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led_pins = [2, 3, 4, 17]

try:
    for i in led_pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)
        print("Led", i, "is on")
        sleep(2)
        GPIO.output(i, GPIO.HIGH)
        sleep(2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

