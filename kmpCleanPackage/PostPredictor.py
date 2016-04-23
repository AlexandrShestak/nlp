# -*- coding: utf-8 -*-
import pickle
import sys
from gensim.models import Word2Vec

from pybrain.tools.xml.networkreader import NetworkReader

reload(sys)
sys.setdefaultencoding("utf-8")

model_name = "myW2VModel"
w2v_model = Word2Vec.load(model_name)


def get_cluster_number(word, cluster_to_words):
    count = 0
    for c in cluster_to_words:
        if word in cluster_to_words[c]:
            return count
        count += 1

class PostPredictor:

    @staticmethod
    def predict(main_words):
        cluster_to_words = pickle.load(open('myW2VModel_claster_1000.p', 'rb'))
        if len(main_words.split()) > 7:
            row_vector_array = [0] * 1000
            for w in main_words.split():
                if w in w2v_model.vocab:
                    row_vector_array[get_cluster_number(w, cluster_to_words)] = 1
            net = NetworkReader.readFrom('trained_network_continue5.xml')
            return net.activate(row_vector_array)
