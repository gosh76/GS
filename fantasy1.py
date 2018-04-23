# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:27:01 2018 by Goldie Sahni
"""


import requests
import csv
from bs4 import BeautifulSoup
page = requests.get('https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2017')
page
soup = BeautifulSoup(page.text, 'html.parser')
soup
s1 = soup.find_all('table')

s1
len(s1)




list1 = []
for s in s1:
    if s.get('id')=='data':
        print('in')
        for f in s.find_all('tr'):
            for t in f.find_all('td'):
                list1.append(t.contents[0])




list1[1].contents[1]

list2 = []
for t in list1:
    list2.append(t.contents)


list2    
