#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Websters Dictionary to Words
author: Craig Warner
"""

# External Imports
import os
import platform
import sys
import argparse
import hjson
import json
#from jsonformatter import JsonFormatter
import time

#
# Functions
#
def IsAllLetters(word):
    return word.isalpha()

#
# Start
#

# CLI Parser
parser = argparse.ArgumentParser(description='Webster to Words')
parser.add_argument("--ifile", help="Template file (.hjson)", default="web.json")
parser.add_argument("--ofile", help="Output file (.hjson)", default="owords.hjson")
parser.add_argument("--all_letters", help="Filter out words which contain numbers and symbols",action="store_true")
parser.add_argument("-v", "--verbose", help="Increase output verbosity",action ="store_true") 

args = parser.parse_args()

print("Info: Args Parse")

all_words = []
web = hjson.load(open(args.ifile))
if args.verbose:
    print("Info: loaded Dictionary")
for word in web: 
    if args.all_letters:
        if IsAllLetters(word):
            all_words.append(word)
        else: 
            if args.verbose:
                print("Info: Dropped:",word)
    else:
        all_words.append(word)

if args.verbose:
    print("Info: Pulled words")

all_words.sort()

if args.verbose:
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