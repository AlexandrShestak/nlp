# -*- coding: utf-8 -*-
import csv
import math
import sys
from decimal import *

from textblob import TextBlob as tb

reload(sys)
sys.setdefaultencoding("utf-8")


def tf(word, blob):
    return Decimal(blob.words.count(word)) / Decimal(len(blob.words))


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    return Decimal(math.log(Decimal(len(bloblist)) /Decimal ((1 + n_containing(word, bloblist)))))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

# now we will search td-idf for each document..
bloblist = []
stars = []
clean_posts = open("clean_text.csv", "r")
with open("clean_text.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        bloblist.append(tb(row['post_text']))
        stars.append(row['stars'])


count = 0
open('main_words.csv', 'w').close()
with open('main_words.csv', 'w') as main_words_file:
    fieldnames = ['main_words', 'stars']
    writer = csv.DictWriter(main_words_file, fieldnames=fieldnames)
    writer.writeheader()
    for i, blob in enumerate(bloblist):
    #print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        words = ''
        for word, score in sorted_words[:15]:
            words += word + ' '
        writer.writerow({'main_words': words, 'stars': stars[i]})
        count += 1
        if count % 100 == 0:
            print count
