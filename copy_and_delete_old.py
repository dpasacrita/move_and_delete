#!/usr/bin/env python
import os
from os.path import isfile, join, exists
from shutil import move
import time

# Declare locations
# filepath = Source location
filepath = '/home/source/'
# dst = Destination
dst = '/home/destination/'

# Get list of files from Source location
files = [f for f in os.listdir(filepath) if isfile(join(filepath, f))]

# Process files and move
for f in files:
    if not exists(join(dst, f)):
        print("Moving file %s" % (join(filepath, f)))
        try:
            move(join(filepath, f), join(dst, f))
        except:
            print("ERROR: Bad file %s" % (join(filepath, f)))

# Now check if any are over 14 days old
# If they are, remove them.
# First get the current time as 'now.'
now = time.time()
# Loop through directory.
for logo in os.listdir(dst):
    fullpath = join(dst, logo)
    # Check if file is older than 1209600 seconds, or 14 days.
    if os.stat(fullpath).st_mtime < (now - 1209600):
        if isfile(fullpath):
            # Don't delete the shortcuts
            if logo.endswith('.lnk'):
                continue
            else:
                print("Deleting file %s" % fullpath)
                try:
                    os.remove(fullpath)
                except:
                    print("ERROR: failed to delete file %s" % fullpath)
