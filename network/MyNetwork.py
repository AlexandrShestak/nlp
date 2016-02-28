# -*- coding: utf-8 -*-
import csv
from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

sentences = []
with open('main_words.csv') as main_words_file:
    reader = csv.DictReader(main_words_file)
    sentence = []
    for row in reader:
        sentence.append(unicode(row['main_words'], "utf-8").split(" "))
        sentences += sentence

num_features = 10  # Word vector dimensionality
min_word_count = 2  # Minimum word count
num_workers = 4  # Number of threads to run in parallel
context = 10  # Context window size
downsampling = 1e-3  # Downsample setting for frequent words

model = Word2Vec(sentences, workers=num_workers, size=num_features,
                 window=context, min_count=min_word_count, sample=downsampling)
model.init_sims(replace=True)
# model_name = "7word_word2vec_model"
# model.save(model_name)

print model.vocab
print model.most_similar(u'девушк')


