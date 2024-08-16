from time import sleep
import RPi.GPIO as GPIO
import requests
import json

btn1 = 22
btn2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

URL='http://localhost:5000/api/shower_toggle'

def toggle_shower(pin):
    r = requests.get(f"{URL}/{pin}")
    print(r.text)

def button_action():
    shower1_button = GPIO.input(btn1)
    shower2_button = GPIO.input(btn2)
    print ("button 1: " + str(shower1_button))
    print ("button 2: " + str(shower2_button))
    # if shower1_button == False:
    #     print('button 1 pressed')
    #     # toggle_shower(btn1)
    # if shower2_button == False:
    #     print('button 2 pressed')
    #     # toggle_shower(btn2)


print ('hi2')
while True:
    button_action()
    sleep(0.2)
