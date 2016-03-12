# -*- coding: utf-8 -*-
from gensim.models import Word2Vec

model_name = "7word_word2vec_model"
model = Word2Vec.load(model_name)

for elem in model.most_similar(u'девушк')[:3]:
    print elem[0]


for elem in model.most_similar(u'подонок')[:3]:
    print elem[0]

for elem in model.most_similar(u'расхотел')[:3]:
    print elem[0]