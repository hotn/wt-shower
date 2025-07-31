import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)

GPIO.output(11, 0)
