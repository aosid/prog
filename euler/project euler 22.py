# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:20:51 2018

@author: vcian
"""

"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

import string

names = open("names.txt")
names_list = names.read()
names.close()

names = names_list.split(sep=",")
for i in range(len(names)):
    names[i] = names[i].strip("\"").lower()
names.sort()

def name_value(name, values = dict(zip(string.ascii_lowercase,range(1,27)))):
    value = 0
    for char in name:
        value += values[char]
    return value

