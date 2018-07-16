#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from os import listdir
from os.path import isfile, join
import sys, string, pprint, json
from itertools import islice
from collections import OrderedDict
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

with open("total_adj_json.json", "r") as total_json_file:
    total_words = json.load(total_json_file)
    total_json_file.close()
    total_words_filtered = dict()
    for word, count in total_words.iteritems():
        if word not in stop_words:
            total_words_filtered[word] = count

    with open("total_adj_json_filtered.json", "w") as total_filtered_file:
        total_words_filtered = OrderedDict(sorted(total_words_filtered.items(), reverse=True, key=lambda(k,v):(v,k)))
        total_filtered_file.write(json.dumps(total_words_filtered))
        total_filtered_file.close()


with open("unique_words.json", "r") as unique_json_file:
    unique_words = json.load(unique_json_file)
    unique_json_file.close()
    unique_words_filtered = dict()
    for word, count in unique_words.iteritems():
        if word not in stop_words:
            unique_words_filtered[word] = count
            
    with open("unique_words_filtered.json", "w") as unique_filtered_file:
        unique_words_filtered = OrderedDict(sorted(unique_words_filtered.items(), reverse=True, key=lambda(k,v):(v,k)))
        unique_filtered_file.write(json.dumps(unique_words_filtered))
        unique_filtered_file.close()