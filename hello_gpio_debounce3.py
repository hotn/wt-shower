import sys
from time import sleep, time
import RPi.GPIO as GPIO
import requests

SHOWER_BUTTON_MAP = {1:22, 2:23}

shower_number = int(sys.argv[1])
button = SHOWER_BUTTON_MAP[shower_number]
time_gate = .4
button_state = 0
button_pending_state = 0
button_last_change = time()
URL='http://localhost:5000/api/shower_toggle'


def listen_for_button_press():
    global button_state
    global button_pending_state
    global button_last_change

    shower_button = GPIO.input(button)
    # print(datetime.now().strftime('%S'))
    # print("button value: " + str(shower1_button))

    # has the button state changed from our last "official" button state
    if shower_button != button_state:
        print("state change: " + str(shower_button))
        if time() - button_last_change < time_gate:
            print("failed time gate")
            return
        # The state change is new. Record it, but do nothing until we're sure it's an actual button push and not just some flakiness
        if shower_button != button_pending_state:
            print("setting pending state: " + str(shower_button))
            button_pending_state = shower_button
            button_last_change = time()
            return

        # The button state is not new, but has it lasted in this state long enough to be confident that it's a legit button push?
        # print("time(): " + str(time()))
        # print("button_last_change: " + str(button_last_change))
        # if time() - button_last_change < .2:
        #     print("failed time gate")
        #     return

        # # Ok, we're pretty sure it's an actual button push now.
        button_state = shower_button

        if shower_button == 1:
            print("PRESS+++++++++++++++++++++")
        else:
            print("DE-PRESS------------------")    

    # if shower2_button != button2_state:
    #     if shower2_button == 1:
    #         print("button 2 press")
    #     else:
    #         print("button 2 de-press")    
    #     button2_state = shower2_button
    else:
        print("reset!!!")
        button_pending_state = shower_button
        button_last_change = time()

def toggle_shower():
    try:
        r = requests.get(f"{URL}/{button}")
        print(r.text)
    except Exception as e:
        print("error: {}".format(e))

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

while True:
    listen_for_button_press()
    sleep(0.2)
