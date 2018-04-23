# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:44:26 2018 by Goldie Sahni
"""


import requests
import csv
from bs4 import BeautifulSoup
"""
page = requests.get('https://moz.com/blog/category/content')
#page
soup = BeautifulSoup(page.text, 'html.parser')
#soup
w1 = soup.find_all('a')
#type(w1)
#w1
#page1 = str(BeautifulSoup(page.content))
list1 = []
for w in w1:
    link = w.get('href',None)
    if link is not None:
        list1.append(link)
"""

listf = []

for n in range(1,25):
    page = requests.get("https://moz.com/blog/category/content?page="+ str(n))
    #print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    w1 = soup.findAll('h2')
    #print(w1)
    for w in w1:
        link = w.find('a')
        try:
            link2 = link.get('href')
            if link2 is not None:
                listf.append(link2)
        except:
            continue
        
            

len(listf)
listf[56]
    

