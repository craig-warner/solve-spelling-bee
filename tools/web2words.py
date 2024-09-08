#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Websters Dictionaly to Words
author: Craig Warner
"""

# External Imports
import os
import platform
import sys
import argparse
import hjson
import json
from jsonformatter import JsonFormatter
import time


#
# Start
#

# CLI Parser
parser = argparse.ArgumentParser(description='Webster to Words')
parser.add_argument("--ifile", help="Template file (.hjson)", default="web.json")
parser.add_argument("--ofile", help="Output file (.hjson)", default="words.hjson")

args = parser.parse_args()

print("Info: Args Parse")

all_words = []
web = hjson.load(open(args.ifile))
print("Info: loaded Dictionary")
for word in web: 
    all_words.append(word)

print("Info: Pulled words")

all_words.sort()

print("Info: Sorted words")

wcnt = 0
olines = []
olines.append("[")

last_word = len(all_words)
line = ""
for w in all_words:
    if wcnt == 10:
        wcnt = 0
        line = line + "\n"
        olines.append(line)
        line = ""
    line = line+"\""+w+"\""
    if wcnt != last_word:
        line = line+","
    wcnt = wcnt + 1
olines.append(line)
olines.append("]")

#ofile_name = args.ofile + ".hjson"
f = open(args.ofile, "w")
for line in olines:
    f.write(line)
f.close()