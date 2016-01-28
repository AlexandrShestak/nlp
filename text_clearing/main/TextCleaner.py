import csv
import string
from nltk.stem.snowball import RussianStemmer
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from nltk.corpus import stopwords
import nltk

nltk.download()

with open('items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        post_text = row['post_text']
        print(post_text)
        exclude = set(string.punctuation)
        post_text = ''.join(ch for ch in post_text if ch not in exclude)
        print(post_text)
        post_text = ''.join([i for i in post_text if not i.isdigit()])
        print(post_text)
        post_words = post_text.split()
        # for word in post_words:
        #     rs = RussianStemmer()
        #     print(word + " " + rs.stem( unicode(word, "utf-8")))
        filtered_words = [word for word in post_words if word not in stopwords.words('russian')]
        print("delete stop words")
        for word in filtered_words:
            print(word)
        post_stars = row['stars']