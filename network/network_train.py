# -*- coding: utf-8 -*-
import csv
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from gensim.models import Word2Vec
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

net = buildNetwork(100, 2, 1)

ds = SupervisedDataSet(100, 1)

model_name = "clean_text_model"
w2v_model = Word2Vec.load(model_name)

with open("main_words_new.csv") as f:
    reader = csv.DictReader(f)
    row_vector_array = []
    for row in reader:
        for w in row['main_words'].split():
            row_vector_array.extend(w2v_model[unicode(w, "utf-8")])
        row_10_vector_array = []
