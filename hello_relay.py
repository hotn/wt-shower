from rpiplc_lib import rpiplc

relay = "RX.7"  # Relay channel for the LED circuit

rpiplc.init("RPIPLC_19R")
rpiplc.pin_mode(relay, rpiplc.OUTPUT)
rpiplc.digital_write(relay, rpiplc.HIGH)  # Relay ON (LED circuit closed)
rpiplc.delay(2000)
rpiplc.digital_write(relay, rpiplc.LOW)   # Relay OFF (LED circuit open)
