import csv
import string
from nltk.stem.snowball import RussianStemmer
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from stop_words import get_stop_words

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
        print(words_after_deleting_stop_words)
        rs = RussianStemmer()
        words_after_stemming = [rs.stem(unicode(w, "utf-8")) for w in words_after_deleting_stop_words]
        print(words_after_stemming)
        text_after_cleaning = ' '.join(words_after_stemming)
        print(text_after_cleaning)
        post_stars = row['stars']