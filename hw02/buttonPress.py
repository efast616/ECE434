#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_8", GPIO.IN)
GPIO.setup("P8_10", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P8_16", GPIO.OUT)
GPIO.setup("P8_18", GPIO.OUT)
GPIO.setup("P8_15", GPIO.OUT)
GPIO.setup("P8_17", GPIO.OUT)

def my_callback(inputbutton):
	if inputbutton == "P8_8":
		GPIO.output("P8_16", GPIO.input("P8_8"))
	if inputbutton == "P8_10":
		GPIO.output("P8_18", GPIO.input("P8_10"))
	if inputbutton == "P8_12":
		GPIO.output("P8_15", GPIO.input("P8_12"))
	if inputbutton == "P8_14":
		GPIO.output("P8_17", GPIO.input("P8_14"))

GPIO.add_event_detect("P8_8", GPIO.BOTH, callback = my_callback, bouncetime=200)
GPIO.add_event_detect("P8_10", GPIO.BOTH, callback = my_callback, bouncetime=200)
GPIO.add_event_detect("P8_12", GPIO.BOTH, callback = my_callback, bouncetime=200)
GPIO.add_event_detect("P8_14", GPIO.BOTH, callback = my_callback, bouncetime=200)

while True:
	continue
