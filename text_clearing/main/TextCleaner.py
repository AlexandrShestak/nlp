# -*- coding: utf-8 -*-
import csv
import string
import math
import sys
from nltk.stem.snowball import RussianStemmer
from textblob import TextBlob as tb
from decimal import *

reload(sys)
sys.setdefaultencoding("utf-8")
from stop_words import get_stop_words


def tf(word, blob):
    return Decimal(blob.words.count(word)) / Decimal(len(blob.words))


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    return Decimal(math.log(Decimal(len(bloblist)) /Decimal ((1 + n_containing(word, bloblist)))))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

count = 0
# next line delete file content
open('text_after_cleaning.csv', 'w').close()
with open('text_after_cleaning.csv', 'w') as data_csv:
    fieldnames = ['post_text', 'stars']
    writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
    writer.writeheader()

    with open('items.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        myPunctuation = u'–«»'
        exclude = set(string.punctuation+myPunctuation)

        for row in reader:
            text_before_cleaning = row['post_text']
            post_text = row['post_text']
            post_text = unicode(post_text, "utf-8")
            post_text = ''.join(ch for ch in post_text if ch not in exclude)
            post_text = ''.join([i for i in post_text if not i.isdigit()])
            post_words = post_text.split()
            stop_words = get_stop_words('ru')
            words_after_deleting_stop_words = [w for w in post_text.split() if not w in stop_words]
            rs = RussianStemmer()
            words_after_stemming = [rs.stem(w) for w in words_after_deleting_stop_words]
            text_after_cleaning = ' '.join(words_after_stemming)
            # this check on empty(null) document
            if text_after_cleaning:
                writer.writerow({'post_text': text_after_cleaning, 'stars': row['stars']})

print '-----------------------'
# now we will search td-idf for each document..
clean_posts = open("text_after_cleaning.txt", "r")
bloblist = []
stars = []
with open("text_after_cleaning.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        bloblist.append(tb(row['post_text']))
        stars.append(row['stars'])

open('main_words.csv', 'w').close()
with open('main_words.csv', 'w') as main_words_file:
    fieldnames = ['main_words', 'stars']
    writer = csv.DictWriter(main_words_file, fieldnames=fieldnames)
    writer.writeheader()
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        words = ''
        for word, score in sorted_words[:7]:
            words += word + ' '
        writer.writerow({'main_words': words, 'stars': stars[i]})
