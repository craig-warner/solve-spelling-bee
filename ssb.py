#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Solve Spelling Bee
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

# Local Imports
from version import __version__

# Issues
# - None

def IsWordHasReq(word,rletter):
    for i in range(0,len(word)): 
        if word[i] == rletter:
            return True
    return False

def IsWordIsOnly(word,aletters):
    for i in range(0,len(word)): 
        in_alist = False
        for a in aletters: 
            if word[i] == a:
                in_alist = True
        if not in_alist:
            return False
    return True 

def IsWord(word,rletter,aletters):
    if len(word) < 4:
        return False
    if IsWordHasReq(word,rletter):
        if IsWordIsOnly(word,aletters):
            return True

def IsPangram(word,aletters):
    for i in range(0,len(aletters)): 
        found = False
        for j in range(0,len(word)): 
            if(word[j] == aletters[i]):
                found = True
        if not found:
            return False
    return True

def ScoreWord(word,aletters):
    # 4 letters => 1 Pts
    # 5 letters => 5 Pts
    # + 7 for pangram
    if len(word) == 4:
        raw_score = 1
    else:
        raw_score = len(word)
    if IsPangram(word,aletters):
        return(raw_score+7)
    else:
        return(raw_score)

    
#
# Start
#

# CLI Parser
parser = argparse.ArgumentParser(description='New York Times Spelling Bee Solver',
            epilog="""
            The source for this Python3 program is publicly available at

            https://github.com/craig-warner/solve-spelling-bee 
            
            Since the script uses a limited English dictionary,
            there may be words it misses. Feel free to change the script to
            use a more complete dictionary.
            """,)
parser.add_argument("--center_letter", help="required letter", default="a")
parser.add_argument("--letter1", help="outside letter number 1", default="b")
parser.add_argument("--letter2", help="outside letter number 2", default="b")
parser.add_argument("--letter3", help="outside letter number 3", default="b")
parser.add_argument("--letter4", help="outside letter number 4", default="b")
parser.add_argument("--letter5", help="outside letter number 5", default="b")
parser.add_argument("--letter6", help="outside letter number 6", default="b")
parser.add_argument("-v", "--verbose", help="Increase output verbosity",action ="store_true") 
parser.add_argument('-V', '--version', action='version', version="%(prog)s ("+__version__+")")

args = parser.parse_args()

aletters = []
aletters.append(args.center_letter.lower())
aletters.append(args.letter1.lower())
aletters.append(args.letter2.lower())
aletters.append(args.letter3.lower())
aletters.append(args.letter4.lower())
aletters.append(args.letter5.lower())
aletters.append(args.letter6.lower())

print("Info: Args Parse")

all_words = hjson.load(open("tools/words.hjson"))
print("Info: loaded Dictionary")
total_words_found = 0
total_score = 0
total_pangrams = 0
for word in all_words: 
    if IsWord(word,args.center_letter,aletters):
        word_score = ScoreWord(word,aletters)
        if IsPangram(word,aletters):
            pstr = "*pangram*"
            total_pangrams = total_pangrams + 1
        else:
            pstr = ""
        str = "Word found: %15s, Value: %d %s" % (word,word_score,pstr)
        print(str)
        total_words_found = total_words_found +1
        total_score = total_score + word_score 
print ("Total number of words found=",total_words_found," Score=",total_score, " Pangrams=", total_pangrams)