# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:02:19 2018

@author: vcian
"""

"""The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?"""

power = 1
count = 1

while True:
    if len(str(9**power)) < power:
        print(count)
        break
    for i in range(2,10):
        if len(str(i**power)) == power:
            count += 1
        if len(str(i**power)) > power:
            continue
    power += 1