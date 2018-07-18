#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re, sys, string, os
from os.path import isfile, join
from os import listdir, rename

# Modified and used to move and fix file extensions
# READMEs got disorganized :(

TEXT_DIR = "./_TEXT"

READMES = sorted([f for f in listdir(TEXT_DIR) if isfile(join(TEXT_DIR, f))])
EXT = 'markdown'

for README in READMES:
    if README.endswith(EXT):
        rename(TEXT_DIR + "/" + README, TEXT_DIR + "/" + README[:(-1 * len(EXT))] + ".md")