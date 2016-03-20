# -*- coding: utf-8 -*-
import csv
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from gensim.models import Word2Vec
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkreader import NetworkReader
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

net = buildNetwork(100, 2, 1)

ds = SupervisedDataSet(100, 1)

model_name = "clean_text_model"
w2v_model = Word2Vec.load(model_name)

with open("main_words_new_new.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if len(row['main_words'].split()) > 10:
            row_vector_array = []
            for w in row['main_words'].split():
                if unicode(w, "utf-8") in w2v_model.vocab:
                    row_vector_array.extend(w2v_model[unicode(w, "utf-8")])
            # print row_vector_array[:100]
            # print row['stars']
            star = int(float(row['stars'])/1000)
            if star > 10:
                ds.addSample(row_vector_array[:100], 11)
            elif star < 0:
                ds.addSample(row_vector_array[:100], -1)
            else:
                ds.addSample(row_vector_array[:100], star)

trainer = BackpropTrainer(net, ds)
# trainer.trainUntilConvergence()
# NetworkWriter.writeToFile(net, 'trained_network1.xml')

maxepochs = 1000
results=[]
for i in range(maxepochs):
    aux = trainer.train()
    print aux

NetworkWriter.writeToFile(net, 'trained_network1.xml')