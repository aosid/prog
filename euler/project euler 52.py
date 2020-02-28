# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:47:53 2018

@author: vcian
"""

"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

i = 1
while True:
    diglist = set(str(i))
    cont = True
    for j in range(2,7):
        if set(str(j * i)) != diglist:
            cont = True
            break
        cont = False
    if not cont:
        for j in range(1,7):
            print("{}*{}={}".format(i,j,i*j))
        raise Exception()
    i += 1
    