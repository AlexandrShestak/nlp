# -*- coding: utf-8 -*-
import csv
import math
import sys
from textblob import TextBlob as tb
from decimal import *
from gensim.models import Word2Vec

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


bloblist = []
stars = []
model_name = "clean_text_model"

w2v_model = Word2Vec.load(model_name)
with open("text_after_cleaning_for_main_words.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        only_in_word2vec_model_words = ''
        for w in row['post_text'].split():
            if unicode(w, "utf-8") in w2v_model.vocab:
                only_in_word2vec_model_words += w + ' '
        print only_in_word2vec_model_words
        bloblist.append(tb(row['post_text']))
        stars.append(row['stars'])

# main_words_file_name = 'main_words_new.csv'
open(main_words_file_name, 'w').close()
with open(main_words_file_name, 'w') as main_words_file:
    fieldnames = ['main_words', 'stars']
    writer = csv.DictWriter(main_words_file, fieldnames=fieldnames)
    writer.writeheader()
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        words = ''
        for word, score in sorted_words[:15]:
            words += word + ' '
        writer.writerow({'main_words': words, 'stars': stars[i]})