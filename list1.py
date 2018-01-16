# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:53:41 2018 by Goldie Sahni
"""


x = [1,2,3]
x
L = eval(input('enter a list'))
L
roll = [2,4,5,67,78]
roll[5]
len(roll)
sum(roll)
max(roll)
min(roll)
for i in range(len(roll)):
    print(roll[i],end=',')

if 5 in roll:
    print('y')

roll.append(16)
sorted(roll)
roll.index(16)
"""end"""
