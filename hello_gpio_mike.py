from datetime import datetime
from time import sleep, time
from math import floor
import RPi.GPIO as GPIO

# btn1 = 22
# btn2 = 23
# button1_state = 0
# button2_state = 0

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(btn1, GPIO.IN)
# GPIO.setup(btn2, GPIO.IN)

# def button_action():
#     global button1_state
#     global button2_state

#     shower1_button = GPIO.input(btn1)
#     shower2_button = GPIO.input(btn2)
#     # print(datetime.now().strftime('%S'))
#     print("button 1 value: " + str(shower1_button))
#     print("button 2 value:    " + str(shower2_button))

#     if shower1_button != button1_state:
#         if shower1_button == 1:
#             print("button 1 press")
#         else:
#             print("button 1 de-press")    
#         button1_state = shower1_button

#     if shower2_button != button2_state:
#         if shower2_button == 1:
#             print("button 2 press")
#         else:
#             print("button 2 de-press")    
#         button2_state = shower2_button





led1 = 19 # shower 1
led2 = 26 # shower 2
led3 = 21 # sink

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

def led_blink():
    if floor(time()) % 2 == 0:
        GPIO.output(led1, 1)
        GPIO.output(led2, 1)
        GPIO.output(led3, 1)
    else:
        GPIO.output(led1, 0)
        GPIO.output(led2, 0)
        GPIO.output(led3, 0)


# print ('hi2')
while True:
    # button_action()
    led_blink()
    sleep(0.2)
