# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:20:55 2018

@author: vcian
"""

"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather interestin
 sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

from string import digits
from itertools import permutations

interestinglist = []

# Works, but is hideous.
#
#for i in range(100,1000,2):
#    remdigs7 = set(digits)
#    nstr = str(i)
#    for dig in nstr:
#        if dig in remdigs7:
#            remdigs7.remove(dig)
#        else:
#            remdigs7 = set()
#    for dig in remdigs7:
#        nstr1 = nstr + dig
#        if int(nstr1[-3:]) % 3 != 0:
#            continue
#        remdigs6 = set(remdigs7)
#        remdigs6.remove(dig)
#        if ('5' not in remdigs6) and ('0' not in remdigs6):
#            continue
#        for dig in remdigs6:
#            if dig not in '05':
#                continue
#            nstr2 = nstr1 + dig
#            remdigs5 = set(remdigs6)
#            remdigs5.remove(dig)
#            for dig in remdigs5:
#                nstr3 = nstr2 + dig
#                if int(nstr3[-3:]) % 7 != 0:
#                    continue
#                remdigs4 = set(remdigs5)
#                remdigs4.remove(dig)
#                for dig in remdigs4:
#                    nstr4 = nstr3 + dig
#                    if int(nstr4[-3:]) % 11 != 0:
#                        continue
#                    remdigs3 = set(remdigs4)
#                    remdigs3.remove(dig)
#                    for dig in remdigs3:
#                        nstr5 = nstr4 + dig
#                        if int(nstr5[-3:]) % 13 != 0:
#                            continue
#                        remdigs2 = set(remdigs3)
#                        remdigs2.remove(dig)
#                        for dig in remdigs2:
#                            nstr6 = nstr5 + dig
#                            if int(nstr6[-3:]) % 17 != 0:
#                                continue
#                            remdigs1 = set(remdigs2)
#                            remdigs1.remove(dig)
#                            perms = permutations(remdigs1)
#                            for perm in perms:
#                                if perm[0] == "0":
#                                    continue
#                                interesting = "".join(perm) + nstr6
#                                interestinglist.append(interesting)

# Try building from right:

def remdigs(n):
    return set(digits) - set(str(n))

def repeats(n):
    for dig in str(n):
        if str(n).count(dig) > 1:
            return True
    return False

for i in range(0,10**3,17):
    if repeats(i):
        continue
    n = str(i)
    for 