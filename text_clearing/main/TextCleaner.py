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
with open('items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text_before_cleaning = row['post_text']
        post_text = row['post_text']
        exclude = set(string.punctuation)
        post_text = ''.join(ch for ch in post_text if ch not in exclude)
        post_text = ''.join([i for i in post_text if not i.isdigit()])
        post_words = post_text.split()
        stop_words = get_stop_words('ru')
        words_after_deleting_stop_words = [w for w in post_text.split() if not w in stop_words]
        rs = RussianStemmer()
        words_after_stemming = [rs.stem(unicode(w, "utf-8")) for w in words_after_deleting_stop_words]
        text_after_cleaning = ' '.join(words_after_stemming)
        if text_after_cleaning:
            with open("text_after_cleaning.txt", "a") as myfile:
                myfile.write(text_after_cleaning + '\n')
                count += 1
        print count, text_after_cleaning
        post_stars = row['stars']

print '-----------------------'
# now we will search td-idf for each document..
clean_posts = open("text_after_cleaning.txt", "r")
bloblist = []
with open("text_after_cleaning.txt") as f:
    lines = f.readlines()
    for line in lines:
        bloblist.append(tb(line))

print bloblist
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:7]:
        print("\tWord: {}, TF-IDF: {}".format(word, score))



