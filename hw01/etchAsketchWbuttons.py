#!/usr/bin/env python3
import argparse
import curses
import Adafruit_BBIO.GPIO as GPIO

def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()

    parser = argparse.ArgumentParser()
    parser.add_argument('--size')
    args = parser.parse_args()
    stdscr.clear()

    GPIO.setup("P8_8", GPIO.IN)
    GPIO.setup("P8_10", GPIO.IN)
    GPIO.setup("P8_12", GPIO.IN)
    GPIO.setup("P8_14", GPIO.IN)

    #add the numbers of the grid on the x and y axis
    for i in range(0, int(args.size)):
    	stdscr.addstr(0,2*i+1,(str(i)+ " "))
    for i in range(0, int(args.size)):
        stdscr.addstr(i+1,0,str(i))
    x = 1;
    y=1;
    stdscr.addstr(y,x,'X')

    stdscr.refresh()
  
    while True:
        key_input = stdscr.getkey()
        if GPIO.input("P8_10"):
            y-=1
            GPIO.output("P8_16", 1)
            if y<1:
                y=1
            stdscr.addstr(y,x,'X')
        if GPIO.input("P8_8"):
            y+=1
            GPIO.output("P8_18", 1)
            if y>int(args.size):
                y=int(args.size)
            stdscr.addstr(y,x,'X')
        if GPIO.input("P8_12"):
            x-=2
            GPIO.output("P8_15", 1)
            if x<1:
                x=1
            stdscr.addstr(y,x,'X')
        if GPIO.input("P8_14"):
            x+=2
            GPIO.output("P8_17", 1)
            if x>(int(args.size)*2):
                x=int(args.size)*2 -1
            stdscr.addstr(y,x,'X')
        if key_input == 'c':
            stdscr.clear()
            main(stdscr)
        if key_input == 'q':
            break	
curses.wrapper(main)
