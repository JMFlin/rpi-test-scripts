import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


GPIO.setup(led_pins, GPIO.OUT)
GPIO.output(led_pins, 1)

led_pins = [2, 3, 4, 17]


try:
    for i in led_pins:
        GPIO.setup(led_pins, GPIO.OUT)
        GPIO.output(led_pins, GPIO.HIGH)
        print("Led", i, "is on")
        sleep(3)
        GPIO.output(i, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

