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
            post_text = ''.join([i for i in post_text if not i.isdigit()])
            post_words = post_text.split()
            stop_words = get_stop_words('ru')
            words_after_deleting_stop_words = [w for w in post_text.split() if not w in stop_words]
            rs = RussianStemmer()
            words_after_stemming = [rs.stem(w) for w in words_after_deleting_stop_words]
            text_after_cleaning = ' '.join(words_after_stemming)
            if text_after_cleaning:
                writer.writerow({'post_text': text_after_cleaning, 'stars': row['stars']})