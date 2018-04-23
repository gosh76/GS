# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:16:15 2018 by Goldie Sahni
"""


def shift1():
    C = input('enter a word')
    N = int(input('enter a number between -52 and 27'))
    import string
    d = string.ascii_lowercase + string.ascii_lowercase
    list1 = []
    for x in C:
        i = d.find(x)
        f = d[i+N]
        list1.append(f)
    return ''.join(list1)

shift1()

