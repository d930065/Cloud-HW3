#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word[0] == '[':
            temp = word[1:15] + ":00:00"
            print ("%s\t%s") % (temp, 1)
