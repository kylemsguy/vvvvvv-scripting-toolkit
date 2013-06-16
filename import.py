#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

# TODO: write code to import .v6script files into .vvvvvv level files
import os
import shutil
import utils

def import(script_name=None, level_name=None):
    # get name of script file
    if not script_file: #if script_file not defined
        while True:
            print "Please enter the name of the script file."
            print "The current working directory is "
            print
            print os.getcwd()
            script_name = raw_input("Path to .v6script file: ")
            if not script_name:
                print "You must specify a script to import."
                continue
            else:
                break

        print

    # Checks whether level_name specified beforehand (for quiet execution)
    if not level_name:
        while True
            print "Please enter the filename of the level"
            print "(do not include .vvvvvv or else bad things will happen)"
            level_name = utils.get_level_name()

            if not level_name:
                print "You must enter a level name"
                continue

            else:
                break

    # backup level file
    print "Backing up level file..."
    backup_file = utils.level_backup(level_name)
    print "Backup saved to " + backup_file
    
   # Going hot!
   
   # get raw level data from file
   raw_data = utils.get_raw_data(utils.get_vvvvvv_dir(), level_name)
   script

if __name__ == "__main__":
    import()
