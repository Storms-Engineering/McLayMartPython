import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
   
    stdscr.addstr("Welcome to McClayMart!")
    stdscr.addstr(1, 0, "Created by Storms-Engineering")
    stdscr.refresh()
    time.sleep(2)
    stdscr.clear()
    #Main loop
    while True:
        curses.echo()
        stdscr.addstr("Please enter name:")
        stdscr.refresh()
        name = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr("Enter cost center:")
        stdscr.refresh()
        costCenter = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr("Please begin scanning items.  Press Cntrl-G when finished.  If you want to remove an item simply delete the line")
        
        #It will double echo if we don't turn this off
        curses.noecho()
        editwin = curses.newwin(5,30, 2,1)
        rectangle(stdscr, 1,0, 1+20+1, 1+30+1)
        stdscr.refresh()

        box = Textbox(editwin)

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        items = box.gather()
    
    
    

wrapper(main)

