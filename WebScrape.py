# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:46:30 2018 by Goldie Sahni
"""

import requests
import csv
from bs4 import BeautifulSoup
f2 = open('C:/Users/HP/Desktop/S1.html','r')
s = f2.read()
#page = requests.get(s)
soup = BeautifulSoup(s, 'html.parser')
s1 = soup.find_all('td')
Names1 = []
Course1 = []
for s,n in zip(s1,range(len(s1))):
    if n % 2 == 0:
        Names1.append(s.contents[0])
    else:
        Course1.append(s.contents[0])

with open('Course1.csv', 'w') as f:
    f1 = csv.writer(f)
    f1.writerow(['Names','Course'])
    for d,f in zip(Names1,Course1):
        f1.writerow([d,f])
        





