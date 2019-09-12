#!/usr/bin/env python3
import argparse
import curses

def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()

    parser = argparse.ArgumentParser()
    parser.add_argument('--size')
    args = parser.parse_args()
    stdscr.clear()

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
        if key_input == 'w':
            y-=1
            if y<1:
                y=1
            stdscr.addstr(y,x,'X')
        if key_input == 's':
            y+=1
            if y>int(args.size):
                y=int(args.size)
            stdscr.addstr(y,x,'X')
        if key_input == 'a':
            x-=2
            if x<1:
                x=1
            stdscr.addstr(y,x,'X')
        if key_input == 'd':
            x+=2
            if x>(int(args.size)*2):
                x=int(args.size)*2 -1
            stdscr.addstr(y,x,'X')
        if key_input == 'c':
            stdscr.clear()
            main(stdscr)
        if key_input == 'q':
            break	
curses.wrapper(main)
