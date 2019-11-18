#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import blynklib

BLYNK_AUTH= 'rtzVtLB2FQOCvrG16EfxvZPCh7KaFZ-I'

blynk = blynklib.Blynk(BLYNK_AUTH)

GPIO.setmode(GPIO.BOARD)

#check your rasberrry pi for these pin numbers

GPIO.setup(11, GPIO.OUT)	#input 1 motor 1
GPIO.setup(13, GPIO.OUT)	#input 2 motor 1
GPIO.setup(15, GPIO.OUT)	#input 1 motor 2
GPIO.setup(16, GPIO.OUT)	#input 2 motor 2

@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
	print(value[0])

@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
	sleeptime = (value[0])

@blynk.handle_event('write V5')			#drive the tank forward
def write_virtual_pin_handler(pin, value):
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)

@blynk.handle_event('write V6')			#drive the tank backward
def write_virtual_pin_handler(pin, value):
	GPIO.output(11, GPIO.LOW) 
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(15, GPIO.LOW) 
	GPIO.output(16, GPIO.HIGH)

@blynk.handle_event('write V7')			#turn towards motor 2 side
def write_virtual_pin_handler(pin, value):
	GPIO.output(11, GPIO.HIGH) 
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW) 
	GPIO.output(16, GPIO.HIGH)

@blynk.handle_event('write V8')
def write_virtual_pin_handler(pin, value):	#turn towards motor 1 side
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)


while True:
	blynk.run()
	time.sleep(sleeptime)
#	GPIO.PWM(19, frequencyA)
#	GPIO.PWM(20, frequencyA)
#	GPIO.PWM(21, frequencyB)
#	GPIO.PWM(22, frequencyB)
#	time.sleep(10)
