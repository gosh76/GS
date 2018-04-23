# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:36:09 2018 by Goldie Sahni
"""

t1 = '   python   '
t2 = t1.rstrip()
t2
t3 = t1.lstrip()
t3
m1 = ['l','h','d']
m1[1] = 'a'
m1
m1.pop(1)
list1 = range(0,100)
del list1
list1 = [x for x in range(1,101)]
list1
list1[-2]
list2 = sorted(list1)
list2[:10]
list3 = sorted(list1,reverse=True)
list3[1]
list2[1]
import numpy as np
np.mean(list1)
def median(c):
    x = sorted(c)
    l = len(x)
    m1 = int(len(x)/2)-1
    m2 = int(len(x)/2)
    med = (x[m1]+x[m2])/2
    return med

median(list1)

def maxi(m):
    k = m[0]
    for x in m:
        if x > k:
            k = x
    k1 = k
    k2 = m[0]
    for x in m:
        if (x > k2) & (x < k1):
            k2 = x
    return k2
   

maxi(list1)

def mini(t):
    t1 = t[0]
    for x in t:
        if x < t1:
            t1 = x
    t2 = t[0]
    for x in t:
        if (x < t2) & (x > t1):
            t2 = x
    return t2

mini(list1)

list2 = [2,3,1,5,6,8,10,10,11,34]
maxi(list2)


from random import randint
random_list = []
for i in range(1,10):
   random_list.append(randint(1,10))

# if I use sort there will be error in case of duplicates
print(sorted(random_list))
print(str(sorted(random_list)[1]) + " " + str(sorted(random_list)[-2]))

#Without sort function ??
print(random_list)
max=0
sec_max = 0
min = 99999999
sec_min = 0
for number in random_list:
   if(number>max):
       sec_max = max
       max = number
   if (number>sec_max) & (number<max):
       sec_max = number
   if(number<min):
       sec_min = min
       min = number
   if (number<sec_min) & (number>min):
       sec_min = number
print(str(sec_min) + " " + str(sec_max))

#save
d1 = input('ask')
d1


#take a no. from user input & shift a list elements by that no.          
# take 5 nos. from user and create histogram of that 5 no.

n1 = int(input('enter'))
n1
list5 = [56,78,43,23,12,89,90,345,123,689,321,4589]
list6 = list5[:]


for x in range(len(list5)-n1):
    list6[x+n1] = list5[x]



for x in range(n1):
    list6[x] = list5[len(list5)-n1+x]

list6


# histogram
listn = []
for x in range(5):
    listn.append(int(input('enter no.')))

listn.sort()
for n in listn:
    print('*'*n)


str_n = str(input('enter separated by ,'))
numbers = [int(x) for x in str_n.split(',')]

numbers

i = max(numbers)
while i >= 1:
    j=0
    while j < len(numbers):
        if numbers[j] - i >= 0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        j += 1
    i -= 1
    print('\n')


#print a triangle for no. of rows given by user.

def pyr(s):
    for i in range(s):
        row = '*'*(2*i + 1)
        print(row.center(2*s))

pyr(6)
pyr(3)


num = int(input('enter'))
ht = num - 1
i = 1
while i <= num:
    if ht > 0:
        print(ht*' ',end='')
        ht -= 1
    print(i*'* ')
    i += 1

#web scraping
import bs4

import requests
import csv
from bs4 import BeautifulSoup

headers = {
   'User-Agent': 'Your Name, example.com',
   'From': 'email@example.com'
}

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 5):
   url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
   pages.append(url)

for item in pages:
   page = requests.get(item, headers= headers)
   soup = BeautifulSoup(page.text, 'html.parser')

   last_links = soup.find(class_='AlphaNav')
   last_links.decompose()

   artist_name_list = soup.find(class_='BodyText')
   artist_name_list_items = artist_name_list.find_all('a')

   for artist_name in artist_name_list_items:
       names = artist_name.contents[0]
       print (names)
       links = 'https://web.archive.org' + artist_name.get('href')

       f.writerow([names, links])



#https://www.consumercomplaints.in/airtel-b100013/page/2

