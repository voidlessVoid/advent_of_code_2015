import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce
import re

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

data = read_input_text()
def part_a(inp):
    dict_of_pos = defaultdict(list)
    pos=[0,0] #x,y
    for idc,c in enumerate(inp):
        dict_of_pos[str(pos)].append(idc)
        if c =='^':
            pos[1]+=1
        elif c =='v':
            pos[1]-=1
        elif c =='>':
            pos[0]+=1
        elif c =='<':
            pos[0]-=1
        #print(c,pos)
    a = [x for x in dict_of_pos if len(dict_of_pos[x])>0]
    print(len(a))

part_a(data)
#2081

def part_b():
    pass
