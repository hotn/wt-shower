from datetime import datetime
from time import sleep, time
import RPi.GPIO as GPIO

def listen_for_button_press():
    global button1_state
    global button2_state
    global button1_pending_state
    global button2_pending_state
    global button1_last_change
    global button2_last_change

    shower1_button = GPIO.input(btn1)
    shower2_button = GPIO.input(btn2)
    # print(datetime.now().strftime('%S'))
    # print("button 1 value: " + str(shower1_button))
    # print("button 2 value:    " + str(shower2_button))

    # has the button state changed from our last "official" button state
    if shower1_button != button1_state:
        print("state change: " + str(shower1_button))
        if get_seconds() - button1_last_change < .4:
            print("failed time gate")
            return
        # The state change is new. Record it, but do nothing until we're sure it's an actual button push and not just some flakiness
        if shower1_button != button1_pending_state:
            print("setting pending state: " + str(shower1_button))
            button1_pending_state = shower1_button
            button1_last_change = get_seconds()
            return

        # The button state is not new, but has it lasted in this state long enough to be confident that it's a legit button push?
        # print("get_seconds(): " + str(get_seconds()))
        # print("button1_last_change: " + str(button1_last_change))
        # if get_seconds() - button1_last_change < .2:
        #     print("failed time gate")
        #     return

        # # Ok, we're pretty sure it's an actual button push now.
        button1_state = shower1_button

        if shower1_button == 1:
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
        button1_pending_state = shower1_button
        button1_last_change = get_seconds()

def get_seconds():
    # TODO: Use unix timestamp or something that isn't just seconds. We don't need to be more granular, but let's avoid bugs from seconds close to each other on different minutes.
    return time()

btn1 = 22
btn2 = 23
button1_state = 0
button2_state = 0
button1_pending_state = 0
button2_pending_state = 0
button1_last_change = get_seconds()
button2_last_change = get_seconds()

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

while True:
    listen_for_button_press()
    sleep(0.2)
