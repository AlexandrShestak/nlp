# -*- coding: utf-8 -*-

import string
import sys
from nltk.stem.snowball import RussianStemmer

reload(sys)
sys.setdefaultencoding("utf-8")
from stop_words import get_stop_words
from gensim.models import Word2Vec


model_name = "myW2VModel"
model = Word2Vec.load(model_name)


class TextCleaner:

   @staticmethod
   def cleanText(textToClean):
        myPunctuation = u'–«»—…'
        exclude = set(string.punctuation + myPunctuation)

        #textToClean = unicode(textToClean, "utf-8")
        textToClean = ''.join(ch for ch in textToClean if ch not in exclude)
        textToClean = ''.join([i for i in textToClean if not i.isdigit()])

        stop_words = get_stop_words('ru')
        words_after_deleting_stop_words = [w for w in textToClean.split()
                                           if (not w in stop_words and w in model.vocab)]

        rs = RussianStemmer()
        words_after_stemming = [rs.stem(w) for w in words_after_deleting_stop_words]
        text_after_cleaning = ' '.join(words_after_stemming)
        #text_after_cleaning = text_after_cleaning.replace(u'кпм', '').replace(u'пмп', '')

        if text_after_cleaning:
            return text_after_cleaning
