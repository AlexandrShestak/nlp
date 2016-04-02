# -*- coding: utf-8 -*-
from __future__ import division
import pickle
from sklearn.cluster import KMeans
from numbers import Number
from pandas import DataFrame
import pickle
import sys, codecs, numpy
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class autovivify_list(dict):
    '''Pickleable class to replicate the functionality of collections.defaultdict'''

    def __missing__(self, key):
        value = self[key] = []
        return value

    def __add__(self, x):
        '''Override addition for numeric types when self is empty'''
        if not self and isinstance(x, Number):
            return x
        raise ValueError

    def __sub__(self, x):
        '''Also provide subtraction method'''
        if not self and isinstance(x, Number):
            return -1 * x
        raise ValueError


cluster_to_words = autovivify_list()
cluster_to_words = pickle.load(open('claster_1000.p', 'rb'))

count = 0
for c in cluster_to_words:
    count += 1
    for w in cluster_to_words[c]:
        print w
    print "\n"
    if count == 10:
        break
