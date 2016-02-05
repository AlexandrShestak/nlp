# -*- coding: utf-8 -*-
import csv

with open('main_words.csv') as main_words_file:
   csv.DictReader(main_words_file)