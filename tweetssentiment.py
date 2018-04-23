# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:58:20 2018 by Goldie Sahni
"""


import numpy as np
import pandas as pd
import csv
from textblob import TextBlob
tweets = pd.read_csv('C:/Users/HP/GSpython/GS/raw.csv')
with open('C:/Users/HP/GSpython/GS/raw.csv',encoding='utf-16') as f:
    f1 = csv.reader(f)
    for t in f1:
        print(t)


