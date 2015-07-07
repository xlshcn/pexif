#!/usr/bin/env python
from pexif import JpegFile
import sys

usage = """Usage: setgps.py filename.jpg lat lng"""

if len(sys.argv) != 4:
    print(usage, file=sys.stderr)
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    ef.set_geo(float(sys.argv[2]), float(sys.argv[3]))
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error opening file:", value, file=sys.stderr)
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print("Error opening file:", value, file=sys.stderr)

try:
    ef.writeFile(sys.argv[1])
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error saving file:", value, file=sys.stderr)

