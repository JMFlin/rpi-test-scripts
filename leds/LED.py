import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led_pins = [2, 3, 4, 17]

#GPIO.setup(led_pins, GPIO.OUT)
#GPIO.output(led_pins, 1)]


try:
    for i in led_pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
        print("Led", i, "is on")
        sleep(3)
        GPIO.output(i, GPIO.LOW)
        sleep(3)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

