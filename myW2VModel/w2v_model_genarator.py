# -*- coding: utf-8 -*-
import csv
from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

sentences = []
file_name = 'text_after_cleaning.csv'
with open(file_name) as main_words_file:
    reader = csv.DictReader(main_words_file)
    for row in reader:
        sentence = []
        post_sentences = unicode(row['post_text'], "utf-8").split(".")
        for post_sentence in post_sentences:
            sentence.append(post_sentence.split(' '))
        sentences += sentence
num_features = 100  # Word vector dimensionality
min_word_count = 15 #Minimum word count
num_workers = 4  # Number of threads to run in parallel
context = 5  # Context window size
downsampling = 1e-3  # Downsample setting for frequent words

model = Word2Vec(sentences, workers=num_workers, size=num_features,
                 window=context, min_count=min_word_count, sample=downsampling)
model.init_sims(replace=True)
model_name = 'myW2VModel'
model.save(model_name)


