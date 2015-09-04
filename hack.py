#!/usr/bin/env python

#  ____                _           _                 _     _    _            _
# |  _ \              | |         | |               | |   | |  | |          | |
# | |_) | ___  _ __ __| | ___ _ __| | __ _ _ __   __| |___| |__| | __ _  ___| | __
# |  _ < / _ \| '__/ _` |/ _ \ '__| |/ _` | '_ \ / _` / __|  __  |/ _` |/ __| |/ /
# | |_) | (_) | | | (_| |  __/ |  | | (_| | | | | (_| \__ \ |  | | (_| | (__|   <
# |____/ \___/|_|  \__,_|\___|_|  |_|\__,_|_| |_|\__,_|___/_|  |_|\__,_|\___|_|\_\

# WARNING:

# THIS IS INTENDED FOR USE ON MAC OS 10.6.8 ONLY --- ONLY USE WITH THIS VERSION!
# This is potentially dangerous. I am not responsible for any damages this may cause.
# 
# PLEASE BACKUP THIS FILE SOMEWHERE SAFE BEFORE RUNNING:
# -------------------------------------------------
# /System/Library/CoreServices/SystemVersion.plist
# -------------------------------------------------

# IF YOU EXPERIENCE ANY PROBLEMS, RESTORE THAT FILE AND PRETEND
# NOTHING EVER HAPPENED!


import os, sys

try:
    print "Which Mac OS version would you like to be running?"
    print "1.) 10.6.8"
    print "2.) 10.7.5"
    print "3.) 10.8.5"
    print "4.) 10.9.5"
    print "4.) 10.10.5"
    valid_choice = False
    while not valid_choice:
        version = raw_input("Type in the number for the version you want to fake: \n")
        if version == "1": version = "10.6.8"; valid_choice = True
        elif version == "2": version = "10.7.5"; valid_choice = True
        elif version == "3": version = "10.8.5"; valid_choice = True
        elif version == "4": version = "10..9.5"; valid_choice = True
        elif version == "5": version = "10.10.5"; valid_choice = True
        else: print "ERROR: Please choose a number from 1 to 5."
        
    if valid_choice:
        f = open("/System/Library/CoreServices/SystemVersion.plist", "w")
        f.write(
'''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ProductBuildVersion</key>
    <string>10K549</string>
    <key>ProductCopyright</key>
    <string>1983-2011 Apple Inc.</string>
    <key>ProductName</key>
    <string>Mac OS X</string>
    <key>ProductUserVisibleVersion</key>
    <string>%s</string>
    <key>ProductVersion</key>
    <string>%s</string>
</dict>
</plist>'''%(version, version))
        f.close()
    else:
        print "ERROR: Try again."
    print "Success! You are now running %s! (teehee)"%(version)
except IOError:
    print "ERROR: You need to run this script as administrator."
    print "Use: sudo python blhack.py"