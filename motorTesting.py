#!/usr/bin/env python3

#import RPi.GPIO as GPIO
import time
import BlynkLib

BLYNK_AUTH= 'N1px31-__MUtyURliOoGUridpQrAvlc3'

blynk = BlynkLib.Blynk(BLYNK_AUTH)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(19, GPIO.OUTPUT)
#GPIO.setup(20, GPIO.OUTPUT)
#GPIO.setup(21, GPIO.OUTPUT)
#GPIO.setup(22, GPIO.OUTPUT)

frequencyA=0
frequencyB=0
#pwm.start(0)

#@blynk.on('read V3')
def v3_write_handler(value):
#	frequencyA = blynk.virtual
	print('current slider value: {}'.format(value[0])
#	frequencyA = 1/(args[0])    	#try this line if it is not working chart of input signals says 1/PWM

#@blynk.handle_event('read V4')

#def v4_write_handler(value):
#	frequencyB = args[0]
#	frequencyB = 1/args[0]		#try this line if it is not working chart of input signals says 1/PWM

while True:
	blynk.run()

#	GPIO.PWM(19, frequencyA)
#	GPIO.PWM(20, frequencyA)
#	GPIO.PWM(21, frequencyB)
#	GPIO.PWM(22, frequencyB)
#	time.sleep(10)
	print(frequencyA)		#debug print statements
	print(", ")			#debug print statements
	print(frequencyB)
