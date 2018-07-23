#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re, sys, string, os, pprint, json, nltk
from os.path import isfile, join
from os import listdir, rename
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.corpus import stopwords
from collections import OrderedDict
from itertools import islice

reload(sys)
sys.setdefaultencoding('utf8')

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return OrderedDict(islice(iterable.iteritems(), n))

def listdir_nohidden(path):
    # https://stackoverflow.com/questions/7099290/how-to-ignore-hidden-files-using-os-listdir
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

def onlyLetters(s):
    no_ascii = "".join(i for i in s if ord(i) < 128)
    return "".join([i for i in no_ascii if not i.isdigit()])

stop_words = set(stopwords.words('english'))
extra_stop_words = ['', ' ', '\x00', 'a', 'www', 'an', 'am', 'the', 'if', 'by', 'be', 'is', 'com', 'to', 'of', 'or', 'with', 'this', 'in', 'with', 'we', 'you', 'youre']
for extra_word in extra_stop_words:
    stop_words.add(extra_word)

def removeStopwords(words):
    for stop_word in stop_words:
        if stop_word in words:
            words.remove(stop_word)

def incrementDict(key, dictionary):
    if key not in dictionary:
        dictionary[key] = 1
    else:
        dictionary[key] += 1

pp = pprint.PrettyPrinter(depth=2)
pprint = pp.pprint

TEXT_DIR = "./_TEXT"
READMES = sorted([f for f in listdir_nohidden(TEXT_DIR) if isfile(join(TEXT_DIR, f))])

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

bi_dict = dict()

for README in READMES:
    readme_file_name = TEXT_DIR + "/" + README
    with open(readme_file_name, "r") as readme_file:
        readme_contents = onlyLetters(readme_file.read())
        words = readme_contents.split(" ")
        removeStopwords(words)
        bi_finder = BigramCollocationFinder.from_words(words)
        bi_collocations = bi_finder.nbest(bigram_measures.likelihood_ratio, 10)
        
        for collocation in bi_collocations:
            if len(collocation[0]) + len(collocation[1]) > 1:
                incrementDict(" ".join(collocation), bi_dict)

if " " in bi_dict:
    bi_dict.pop(" ")

bi_dict_sorted = OrderedDict(sorted(bi_dict.items(), reverse=True, key=lambda(k,v):(v,k)))
bi_dict_json = json.dumps(take(1000, bi_dict_sorted))

with open("bigram_words.json", "w") as bigram_file:
    bigram_file.write(bi_dict_json)
    bigram_file.close()