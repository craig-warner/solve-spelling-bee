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
from jsonformatter import JsonFormatter
import time

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
    
#
# Start
#

# CLI Parser
parser = argparse.ArgumentParser(description='Solce Spelling Bee')
parser.add_argument("--center_letter", help="Required Letter", default="a")
parser.add_argument("--letter1", help="outside letter number 1", default="b")
parser.add_argument("--letter2", help="outside letter number 1", default="b")
parser.add_argument("--letter3", help="outside letter number 1", default="b")
parser.add_argument("--letter4", help="outside letter number 1", default="b")
parser.add_argument("--letter5", help="outside letter number 1", default="b")
parser.add_argument("--letter6", help="outside letter number 1", default="b")

args = parser.parse_args()

aletters = []
aletters.append(args.center_letter)
aletters.append(args.letter1)
aletters.append(args.letter2)
aletters.append(args.letter3)
aletters.append(args.letter4)
aletters.append(args.letter5)
aletters.append(args.letter6)

print("Info: Args Parse")

all_words = hjson.load(open("tools/words.hjson"))
print("Info: loaded Dictionary")
for word in all_words: 
    if IsWord(word,args.center_letter,aletters):
        print("Word Found:",word)