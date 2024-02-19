import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import curses
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
    '''
    stdscr.addstr("Welcome to McClayMart!")
    stdscr.addstr(1, 0, "Created by Storms-Engineering")
    stdscr.refresh()
    curses.beep();
    time.sleep(1)
    stdscr.clear()
    '''
    #Main loop
    while True:
        #TODO: open database with specific vendor, DNOW, MRC etc.
        
        curses.echo()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        stdscr.attron(curses.color_pair(1))
        '''
        stdscr.addstr("Please enter name:")
        stdscr.refresh()
        name = stdscr.getstr().decode(encoding="utf-8")
        stdscr.clear()
        stdscr.addstr("Enter cost center:")
        stdscr.refresh()
        costCenter = stdscr.getstr().decode(encoding="utf-8")
        stdscr.clear()
        title = "Name:{}  Cost Center:{}".format(name, costCenter)
        stdscr.addstr(0,0,title)
        '''
        stdscr.addstr(1,0,"Please begin scanning items.")
        stdscr.move(2,0)
        #Build place for showing items scanned
        item_pad = curses.newpad(35, 150)
        rectangle(stdscr, 3,0, 1+35+1, 1+150+1)
        stdscr.refresh()
        
        #Sub loop for scanning items
        stdscr.move(2,0)
        item_num = stdscr.getstr().decode(encoding="utf-8")
        item_count = 0;
        while item_num != "":
            item_pad.move(item_count,0)
            item_pad.addstr(item_num)
            # Displays a section of the pad in the middle of the screen.
            # (0,0) : coordinate of upper-left corner of pad area to display.
            # (5,5) : coordinate of upper-left corner of window area to be filled
            #         with pad content.
            # (20, 75) : coordinate of lower-right corner of window area to be
            #          : filled with pad content.
            item_pad.refresh( 0,0, 4,1, 35,150)
            stdscr.move(2,0)
            stdscr.clrtoeol()
            stdscr.refresh()
            item_num = "";
            item_num = stdscr.getstr().decode(encoding="utf-8")
            item_count += 1

        #Probably won't use this method
        #It will double echo if we don't turn this off
        '''
        curses.noecho()
        editwin = curses.newwin(5,30, 2,1)
        
        
        
        box = Textbox(editwin)

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        items = box.gather()'''
        exit();
    
    

wrapper(main)

