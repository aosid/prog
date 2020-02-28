# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:47:44 2018

@author: vcian
"""

"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

current_date = [7,1,1900]

lmonths = [1,3,5,7,8,10,12]
smonths = [4,6,9,11]

lengths = {2: 28}
for m in lmonths:
    lengths[m] = 31
for m in smonths:
    lengths[m] = 30

def is_leap_year(y):
    return ((y % 4 == 0) & ((y % 100 != 0) or (y % 400 == 0)))

def next_sunday(date):
    year = date[2]
    month = date[1]
    day = date[0] + 7
    if day > lengths[month]:
        day = day % lengths[month]
        month = month + 1
    if month == 13:
        month = 1
        year += 1
        if is_leap_year(year):
            lengths[2] = 29
        else:
            lengths[2] = 28
    return [day,month,year]

def all_sundays(date):
    count = 0
    while date[2] < 2001:
        if ((date[2] > 1900) & (date[0] == 1)):
            count += 1
            print(date)
        date = next_sunday(date)
    return count