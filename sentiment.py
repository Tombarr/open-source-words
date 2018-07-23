#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re, sys, string, os, pprint, json, nltk
from os.path import isfile, join
from os import listdir, rename
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.corpus import stopwords
from collections import OrderedDict
from itertools import islice
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

pp = pprint.PrettyPrinter(depth=2)
pprint = pp.pprint

# definitely easier than training my own classifier
sid = SentimentIntensityAnalyzer()

summary = { "positive":0, "neutral":0, "negative": 0, "compound": [ ]}
README_DIR = "./_FULLTEXT"
READMES = sorted([f for f in listdir_nohidden(README_DIR) if isfile(join(README_DIR, f))])

for README in READMES:
    readme_file_name = README_DIR + "/" + README
    with open(readme_file_name, "r") as readme_file:
        readme_contents = onlyLetters(readme_file.read())
        sentences = sent_tokenize(readme_contents)
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            if ss["compound"] == 1:
                print('Very positive sentiment score %f' % ss["compound"])
                print(sentence)
            #summary["compound"].append(ss["compound"])
            if ss["compound"] == 0.0:
                summary["neutral"] += 1
            elif ss["compound"] > 0.0:
                summary["positive"] += 1
            else:
                summary["negative"] += 1

summary["compound_mean"] = mean(summary["compound"])
pprint(summary)

#summary_json = json.dumps(summary)

#with open("vader_sentiment.json", "w") as summary_json_file:
#    summary_json_file.write(summary_json)
#    summary_json_file.close()