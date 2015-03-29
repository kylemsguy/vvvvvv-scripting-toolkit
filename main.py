#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import sys
import extract
import import_script
import utils

def interactive_menu():
    while True:
        print "Please select which mode you wish to use: "
        print "1. Extract script from level file"
        print "2. Import script into level file"
        print "q. Exit"
        answer = raw_input("Selection: ")
        if answer == '1':
            extract.extract()
            quit()
        elif answer == '2':
            import_script.import_script()
            quit()
        elif answer == 'q':
            print "Quitting..."
            quit()
        else:
            print "Invalid selection"
            continue

# Initialize variables
mode = None
vvvvvv_dir = None
level_name = None
script_file = None

# Check for command line parameters
args = sys.argv

params = utils.command_switches(args)

if not params:
    quit()

elif params == 1:
    interactive_menu()
