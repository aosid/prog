# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:19:06 2018

@author: vcian
"""

"""The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

# Note: as each digit will become the final digit in the process of right truncation,
# the only possible values for internal digits are 1, 3, 7, and 9. Only 2, 3, 5, and 7 may lead/conclude.
# This info may be more annoying to implement than they're worth

#Since there are more restrictions on the digits of the right truncatable prime, there are fewer. Do them first.


#from time import sleep
from primes import is_prime

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def ltrunc_check(n):
    nstr = str(n)
    for i in range(len(nstr)):
        if not is_prime(nstr[i:]):
            return False
    return True

@memoize
def rtrunc_check(n):
    nstr = str(n)
    for i in range(len(nstr)):
        if not is_prime(nstr[:len(nstr)-i]):
            return False
    return True

def trunc_check(n):
    return (ltrunc_check(n) and rtrunc_check(n))

plist = [2,3,5,7]

def lappend(plist):
    diglist = ["1","2","3","5","7","9"]
    while True:
        checklist = list(plist)
        for p in plist:
            for dig in diglist:
                newstr = dig + str(p)
                if int(newstr) not in plist:
                    if is_prime(newstr):
                        plist.append(int(newstr))
        if checklist == plist:
            break
    return plist

def rappend(plist):
    diglist = ["1","2","3","5","7","9"]
    while True:
        checklist = list(plist)
        for p in plist:
            for dig in diglist:
                newstr = str(p) + dig
                if int(newstr) not in plist:
                    if is_prime(newstr):
                        plist.append(int(newstr))
        if checklist == plist:
            break
        print(plist)
    return plist