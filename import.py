#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

# TODO: write code to import .v6script files into .vvvvvv level files
import os
import utils

def import(script_name=None, level_name=None):
    # get name of script file
    if not script_file: #if script_file not defined
        print "Please enter the name of the script file."
        print "The current working directory is "
        print
        print os.getcwd()
        script_name = raw_input("Path to .v6script file: ")

        print

    if not level_name:
        print "Please enter the name of the level (do not include .vvvvvv)"

   

if __name__ == "__main__":
    import()