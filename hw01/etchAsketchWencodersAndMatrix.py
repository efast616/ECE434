#!/usr/bin/env python3
import argparse
import curses
import Adafruit_BBIO.GPIO as GPIO
from Adagruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import smbus
import OS
import time

os.system("config-pin P8_33 qep")
os.system("config-pin P8_35 qep")
os.system("config-pin P8_11 gpio")
os.system("config-pin P8_12 gpio")
os.system("config-pin P8_41 qep")
os.system("config-pin P8_42 qep")
    
i2cbus= smbus.SMBus(2)
led_addr= 0x70
bus.write_byte_data(led_addr, 0x21, 0)
bus.write_byte_data(led_addr, 0x81, 0)
bus.write_byte_data(led_addr, 0xe7, 0)

myEncoderx = RotaryEncoder(eQEP2b)
myEncoderx.setAbsolute()
myEncoderx.enable()
myEncodery = RotaryEncoder(eQEP1)
myEncodery.setAbsolute()
myEncodery.enable()

cur_positionx = myEncoderx.position
cur_positiony = myEncodery.position

ledx=0
ledy=0
row=0
column=0

ledMatrix=[0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

while True:
	if myEncodery.position<0:
		ledy-=1
		if ledy<0:
			ledy=0
		column = 2**ledy
		row = 2*ledx
		ledMatrix[row]= ledMatrix[row] | column
	if myEncodery.position>0:
		ledy+=1
		if ledy>7:
       	        	ledy=7
		column = 2**ledy
		row = 2*ledx
		ledMatrix[row]= ledMatrix[row] | column
       	if myEncoderx.position<0:
		ledx-=1
		if ledx<0:
			ledx=0
		column = 2**ledy
		row = 2*ledx
		ledMatrix[row]= ledMatrix[row] | column
       	if myEncoderx.position>0:
		ledx+=1
		if ledx>7:
			ledx=7	
		column = 2**ledy
		row = 2*ledx
		ledMatrix[row]= ledMatrix[row] | column
	
	myEncoderx.position=0
	myEncodery.position=0
				
	bus.write_i2c_block_data(led_addr, 0, ledMatrix)


