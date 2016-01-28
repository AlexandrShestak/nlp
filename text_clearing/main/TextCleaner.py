import csv
import string
from nltk.stem.snowball import RussianStemmer
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from nltk.corpus import stopwords
import nltk
from stop_words import get_stop_words

with open('items.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text_before_cleaning = row['post_text']
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

        stop_words = get_stop_words('ru')
        for sw in stop_words:
            print(sw)

        text_after_cleaning = ""
        for word in post_words:
             if word not in stop_words:
                text_after_cleaning += word + " "


        print("text before cleaning")
        print(text_before_cleaning)
        print("text after delete stop words")
        print(text_after_cleaning)
        post_words = text_after_cleaning.split(" ")
        text_after_stemming = ""
        rs = RussianStemmer()
        for word in post_words:
            text_after_stemming += rs.stem(unicode(word, "utf-8")) + " "
        print("text after STEMMING")
        print(text_after_stemming)


        # filtered_words = [word for word in post_words if word not in stop_words]
        # print("delete stop words")

        # for word in filtered_words:
        #     print(word)
        post_stars = row['stars']