#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import blynklib

BLYNK_AUTH= 'TC93qr2a6AvBZ9fB8dVu4-WKEj6-PTbp'

blynk = blynklib.Blynk(BLYNK_AUTH)

GPIO.setmode(GPIO.BOARD)

#check your rasberrry pi for these pin numbers

GPIO.setup(11, GPIO.OUT)	#input 1 motor 1
GPIO.setup(13, GPIO.OUT)	#input 2 motor 1
GPIO.setup(15, GPIO.OUT)	#input 1 motor 2
GPIO.setup(16, GPIO.OUT)	#input 2 motor 2

@blynk.handle_event('write V5')			#drive the tank forward
def write_virtual_pin_handler(pin, value):
	pwm0.start(defaultSpeed) 			#Right motor
	pwm1.start(0)
	pwm2.start(round(defaultSpeed*offset)) 		#Left motor
	pwm3.start(0)

@blynk.handle_event('write V6')			#drive the tank backward
def write_virtual_pin_handler(pin, value):
        pwm0.start(0)
        pwm1.start(defaultSpeed)
        pwm2.start(0)
        pwm3.start(round(defaultSpeed*offset))


@blynk.handle_event('write V7')			#turn the tank left
def write_virtual_pin_handler(pin, value):
        pwm0.start(round(defaultSpeed/1.75))
        pwm1.start(0)
        pwm2.start(0)
        pwm3.start(round(defaultSpeed*offset/1.75))



@blynk.handle_event('write V8')
def write_virtual_pin_handler(pin, value):	#turn the tank right
        pwm0.start(0)
        pwm1.start(round(defaultSpeed/1.75))
        pwm2.start(round(defaultSpeed*offset/1.75))
        pwm3.start(0)

@blynk.handle_event('write V9')                 #stop the tank
def write_virtual_pin_handler(pin, value):
	pwm0.start(0)
	pwm1.start(0)
	pwm2.start(0)
	pwm3.start(0)

pwm0 = GPIO.PWM(11, 100)
pwm1 = GPIO.PWM(13, 100)
pwm2 = GPIO.PWM(15, 100)
pwm3 = GPIO.PWM(16, 100)
pwm0.start(0)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
defaultSpeed = 100
offset = 0.78

while True:
	blynk.run()
#	time.sleep(sleeptime)
#	GPIO.PWM(19, frequencyA)
#	GPIO.PWM(20, frequencyA)
#	GPIO.PWM(21, frequencyB)
#	GPIO.PWM(22, frequencyB)
#	time.sleep(10)
