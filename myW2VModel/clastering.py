# -*- coding: utf-8 -*-
from __future__ import division
from gensim.models import Word2Vec
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

model = Word2Vec.load('clean_text_model')
model.vocab

vector_file = open('vector_file', 'w')
count = 0
for word in model.vocab:
    count += 1
    vector_file.write(str(word).rstrip('\n'))
    vector_file.write(' '.rstrip('\n'))
    vector_file.write(str(model[word]).rstrip('\n').replace('[', '').replace(']', '').replace('\n', ''))
    vector_file.write("\n")
    # if count == 100:
    #     vector_file.close()
    #     break
