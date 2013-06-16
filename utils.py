## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import os
import sys
from HTMLParser import HTMLParser
from os.path import expanduser
from time import strftime

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def get_vvvvvv_dir():
    home_dir = expanduser("~") # Gets home dir
    
    if sys.platform.startswith("linux"):
        vvvvvv_dir = home_dir + "/.vvvvvv/"

    elif sys.platform.startswith("win"):
        vvvvvv_dir = home_dir + "/Documents/VVVVVV/"

    elif sys.platform.startswith("darwin"):
        vvvvvv_dir = home_dir + "/Documents/VVVVVV/"

    else:
        print "Error: unsupported platform"
        quit()

    return vvvvvv_dir

def get_raw_data(vvvvvv_dir, level_name):
    # get level data
    filename = level_name + ".vvvvvv"    
    level_path = vvvvvv_dir + filename
    try:
        with open(level_path, 'r') as infile:
            return infile.readlines()
    except IOError:
        return False

def get_script_data(raw_data):
    # get script data
    for line in raw_data:
        if "<script>" in line:
            return line

    if not script_data:
        return False

def get_script_line(raw_data, script_data):
    for i in range(len(raw_data)):
        if "<script>" in raw_data[i]:
            
            return True
        else:
            continue

    return False

def cleanup_data(script_data):
    # remove <script></script> tags
    tagless_data = strip_tags(script_data)

    # remove any leading spaces etc
    sanitized_data = tagless_data.lstrip()

    # split into lines by pipe chars
    final_data = sanitized_data.split('|')

    return final_data

def get_level_name():
    level_name = raw_input("ID of level (do not include extension): ")
    return level_name

def level_backup(level_name):
    # check if backup dir exists
    leveldir = get_vvvvvv_dir()
    backupdir = get_vvvvvv_dir() + "vvvvvv_level_backups/"
    if not os.path.isdir(backupdir):
        # make the dir
        os.mkdir(backupdir)

    curr_time = strftime("%Y-%m-%d %H%M")
    shutil.copyfile(level_dir + level_name + ".vvvvvv",
                    backupdir + level_name + curr_time + ".vvvvvv")

    return backupdir + level_name + curr_time + ".vvvvvv"
