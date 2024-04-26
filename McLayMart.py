import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper
import curses
import time

#This is loaded from the disk and is shouldn't be changed onced loaded
database = list()

#This is the one for the current checkout list which is eventually written to the disk


#Loads a database for DNOW
def load_database(fileName):
    f = open(fileName, "r")
    for line in f:
        data = line.split(",")
        dataDict = {
            "sap_num" : data[0].strip(),
            "description": data[1].strip(),
            "part_num": data[2].strip()
        }
        database.append(dataDict)
    f.close()

def main(stdscr):
    #Setup curses colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(1))

    # Clear screen
    stdscr.clear()
    stdscr.addstr("Welcome to McClayMart!")
    stdscr.addstr(1, 0, "Created by Storms-Engineering")
    stdscr.addstr(2, 0, "Loading database...")
    stdscr.refresh()
    time.sleep(2)
    stdscr.clear()
    
    #Load ssp data
    load_database("ssp_data.csv")

   
    curses.echo()
    

    #Main loop
    while True: 
        items_purchased = list()
        stdscr.clear()
        stdscr.addstr("Please enter name:")
        stdscr.refresh()
        name = stdscr.getstr().decode(encoding="utf-8")
        if name == "exit":
            exit()
        stdscr.clear()
        stdscr.addstr("Enter cost center:")
        stdscr.refresh()
        costCenter = stdscr.getstr().decode(encoding="utf-8")
        stdscr.clear()
        title = "Name:{}  Cost Center:{}".format(name, costCenter)
        stdscr.addstr(0,0,title)
        stdscr.addstr(1,0,"Please begin scanning items. Press Enter with an empty part number to finish.")
        stdscr.addstr(2,0, "Enter part num:")
        stdscr.addstr(3,0,"Item #")
        stdscr.addstr(3,30,"Description")
        #stdscr.addstr(3,100,"Quantity")
        #Build place for showing items scanned
        item_pad = curses.newpad(35, 150)
        rectangle(stdscr, 4,0, 1+35+1, 1+150+1)
        stdscr.refresh()
        
        #Sub loop for scanning items
        stdscr.move(2,15)
        #We have to remove dashes because they are not dashed in the database
        item_num = stdscr.getstr().decode(encoding="utf-8").replace("-","").upper()
        item_count = 0;
        while item_num != "":
            item_pad.move(item_count,0)
            #We can write this here because it will always be written
            item_pad.addstr(item_num)
            #Here we search for the sap or part# and search for it
            desc = ""
            for item in database:
                if item["sap_num"] == item_num or item["part_num"] == item_num:
                    #Print out information about part
                    #TODO eventually update quantity instead of having duplicate lines oh yeah bb
                    desc =  item["description"]
                    items_purchased.append(item)
                    break
            if desc == "":
            #If we don't find it ask for a description
                stdscr.move(2,0)
                stdscr.clrtoeol()
                stdscr.refresh()
                stdscr.addstr("Please enter description for item:")
                stdscr.refresh()
                desc = stdscr.getstr().decode(encoding="utf-8")
                #We need to manually add this item since it is not in the database for file writing purposes
                dataDict = {
                    "sap_num" : "N/A",
                    "description": desc,
                    "part_num": item_num
                    }
                items_purchased.append(dataDict)

                    
            item_pad.addstr(item_count, 30, desc)
            # Displays a section of the pad in the middle of the screen.
            # (0,0) : coordinate of upper-left corner of pad area to display.
            # (5,5) : coordinate of upper-left corner of window area to be filled
            #         with pad content.
            # (20, 75) : coordinate of lower-right corner of window area to be
            #          : filled with pad content.
            item_pad.refresh( 0,0, 5,1, 35,150)
            stdscr.addstr(2,0, "Enter part num:")
            stdscr.clrtoeol()
            stdscr.refresh()
            item_num = "";
            item_num = stdscr.getstr().decode(encoding="utf-8").upper()
            item_count += 1


        #Write out items_purchased to file
        f = open("items_purchased.csv", "a")
        #f.write("SAP #, Description, Part Num, Cost Center/AFE, Name \n")
        for item in items_purchased:
            f.write(item["sap_num"] + "," + item["description"] + "," + item["part_num"] + "," + costCenter + "," + name + "\n")
        f.close()
        stdscr.clear();
        stdscr.addstr(1,0, "Thanks for you purchase, items added to database.")
        stdscr.refresh()
        time.sleep(2)
    
wrapper(main)

