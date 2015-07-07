#!/usr/bin/env python
from pexif import JpegFile
import sys

usage = """Usage: remove_metadata.py filename.jpg"""

if len(sys.argv) != 4:
    print(usage, file=sys.stderr)
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    ef.remove_metadata(paranoid=True)
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
