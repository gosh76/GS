# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:02:58 2018 by Goldie Sahni
"""


import requests
import csv
from bs4 import BeautifulSoup
page = requests.get('http://rezo.ai/#howrezoworks')
page
soup = BeautifulSoup(page.text, 'html.parser')
soup
w1 = soup.find_all('p')

#w1[0].contents[0]
#w1[1].contents[0]
#w1[1].contents[0].replace('\n\t\t\t\t\t\t\t\t\t',' ')
#w1[0].contents[0].replace('\n\t\t\t\t\t\t\t\t\t',' ')

list1 = []
for w in w1:
    list1.append(w.contents[0].replace('\n\t\t\t\t\t\t\t\t\t',' '))

list1[0]
len(list1)
list1[4]
list1[3]
list1[1]
list1[2]
