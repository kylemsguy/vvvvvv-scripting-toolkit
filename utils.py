## Copyright (c) 2013 Kyle Zhou
##
## See the file license.txt for copying permission.

import sys
from HTMLParser import HTMLParser

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

def getos():
    if sys.platform.startswith("win"):
        return 1

    elif sys.platform.startswith("linux"):
        return 0

    elif sys.platform.startswith("darwin"):
        return 2

    else:
        return -1

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

def cleanup_data(script_data):
    # remove <script></script> tags
    tagless_data = strip_tags(script_data)

    # remove any leading spaces etc
    sanitized_data = tagless_data.lstrip()

    # split into lines by pipe chars
    final_data = sanitized_data.split('|')

    return final_data

def level_backup(level_name=None):
    if not level_name:
        return False
    else:
        pass
