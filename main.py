#!/usr/bin/env python
## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import sys

def display_help():
    print "Help shall be implemented soon"
    exit()

# Initialize variables
vvvvvv_dir = None
level_name = None
script_file = None

# Check for command line parameters
args = sys.argv()
if "--help" in args:
    display_help()

else:
    skip = 0
    for i in range(len(args)):
        if skip:
            skip -= 1
            continue
        
        if args[i] == "-d":
            vvvvvv_dir = args[i + 1]
            skip = 1

        elif args[i] == "-l":
            level_name = args[i + 1]
            skip = 1

        elif args[i] == "-s":
            script_file = args[i + 1].strip('"')
            skip = 1

        else:
            print "invalid command line argument"
            display_help()
