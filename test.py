#!/usr/bin/env python3
#import RPi.GPIO as GPIO
import blynklib
import time

BLYNK_AUTH = 'N1px31-__MUtyURliOoGUridpQrAvlc3'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V3 write event
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
#	print(WRITE_EVENT_PRINT_MSG.format(pin, value))
	print("x value: " + str(value[0]))
    
# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
#	print(WRITE_EVENT_PRINT_MSG.format(pin, value))
	print("y value: " + str(value[0]))
    
###########################################################
# infinite loop that waits for event
###########################################################
while True:
	blynk.run()

