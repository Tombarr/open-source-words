#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from os import listdir
from os.path import isfile, join
import sys, string, pprint, json
from itertools import islice
from collections import OrderedDict
import nltk

reload(sys)  
sys.setdefaultencoding('utf8')

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return OrderedDict(islice(iterable.iteritems(), n))

def removeNonAscii(s):
    return "".join(i for i in s if ord(i) < 128)

TEXT_DIR = "./_TEXT"

READMES = sorted([f for f in listdir(TEXT_DIR) if isfile(join(TEXT_DIR, f))])

printable = set(string.printable)

total_word_count = dict()
unique_word_count = dict()

for README in READMES:
    readme_file_name = TEXT_DIR + "/" + README
    with open(readme_file_name, "r") as readme_file:
        readme_contents = removeNonAscii(readme_file.read())
        readme_contents = ''.join([i for i in readme_contents if not i.isdigit()])
        words = readme_contents.split(" ")
        unique_words = set(words)

        for word in words:
            if '\x00' in word:
                continue
            if word not in unique_word_count:
                total_word_count[word] = 1
            else:
                total_word_count[word] += 1

        for word in unique_words:
            if '\x00' in word:
                continue
            if word not in unique_word_count:
                unique_word_count[word] = 1
            else:
                unique_word_count[word] += 1

unique_word_count.pop('')
total_word_count.pop('')

unique_word_count_dict = unique_word_count
total_word_count_dict = total_word_count

unique_word_count = OrderedDict(sorted(unique_word_count.items(), reverse=True, key=lambda(k,v):(v,k)))
total_word_count = OrderedDict(sorted(total_word_count.items(), reverse=True, key=lambda(k,v):(v,k)))

pp = pprint.PrettyPrinter(depth=2)

ADJ_POS = [ "JJ", "JJR", "JJS", "RB", "RBR", "RBS" ] # adjective or adverb

print("%d unique words" % len(unique_word_count))

unique_word_pos = nltk.pos_tag(list(unique_word_count))

unique_adjs = list(filter(lambda word: word[1] in ADJ_POS, unique_word_pos))

print("%d unique adjectives and adverbs" % len(unique_adjs))

unique_adj_count = dict()
total_adj_count = dict()
for tags in unique_adjs:
    adj = tags[0]
    unique_adj_count[adj] = unique_word_count_dict[adj]
    total_adj_count[adj] = total_word_count_dict[adj]

unique_adj_count = OrderedDict(sorted(unique_adj_count.items(), reverse=True, key=lambda(k,v):(v,k)))
total_adj_count = OrderedDict(sorted(total_adj_count.items(), reverse=True, key=lambda(k,v):(v,k)))

unique_adj_json = json.dumps(take(1000, unique_adj_count))
total_adj_json = json.dumps(take(1000, total_adj_count))

with open("unique_words.json", "w") as unique_word_file:
    unique_word_file.write(unique_adj_json)
    unique_word_file.close()

with open("total_adj_json.json", "w") as total_word_file:
    total_word_file.write(total_adj_json)
    total_word_file.close()