# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:38:10 2018

@author: vcian
"""

"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""

i = 1
dig_list = []
while len(dig_list) < 1000001:
    dig_list += list(str(i))
    i += 1