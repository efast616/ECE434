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

GPIO.add_event_detect("P8_15", GPIO.RISING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect("P8_17", GPIO.RISING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect("P8_16", GPIO.RISING, callback=my_callback, bouncetime=200)
GPIO.add_event_detect("P8_18", GPIO.RISING, callback=my_callback, bouncetime=200)

def my_callback(inputbutton):
	if(inputbutton == "P8_15")
		GPIO.output("P8_15", GPIO.HIGH)
	if(inputbutton == "P8_17")
		GPIO.output("P8_17", GPIO.HIGH)
	if(inputbutton == "P8_16")
		GPIO.output("P8_16", GPIO.HIGH)
	if(inputbutton == "P8_18")
		GPIO.output("P8_18", GPIO.HIGH)

while True:
	continue
