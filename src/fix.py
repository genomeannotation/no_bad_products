#!/usr/bin/env python

import re
from plurals import keep_terminal_s

def contains_3_or_more_numbers_in_a_row(word):
    numcount = 0
    numrun = False
    for letter in word:
        if letter in '0123456789':
            numrun = True
            numcount += 1
            if numcount >= 3:
                return True
        else:
            numcount = 0
            numrun = False
    return False

def remove_protein_homolog(line):
    if "protein homolog" in line:
        line = re.sub("protein homolog", "", line)
    if "homolog protein" in line:
        line = re.sub("homolog protein", "", line)
    if "homolog" in line:
        line = re.sub("homolog", "", line)
    # make sure we didn't leave extra whitespace
    fields = line.strip().split()
    return " ".join([f.strip() for f in fields])

def fix_plural(anno):
    if anno in keep_terminal_s:
        return anno
    else:
        # TODO
        return "idk"