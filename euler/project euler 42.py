# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:02:44 2018

@author: vcian
"""

"""The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value
for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then
we shall call the word a triangle word.

Using p042_words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?"""

from string import ascii_uppercase as upper

file = open("p042_words.txt")
wordlist = file.read().replace('"',"").split(",")
file.close()

charscores = {}
for char in upper:
    charscores[char] = upper.index(char) + 1

wordscores = []
for word in wordlist:
    total = 0
    for char in word:
        total += charscores[char]
    wordscores.append(total)
    
maxscore = max(wordscores)    

trilist = []
i = 1
n = 1
while n <= maxscore:
    trilist.append(n)
    n = (i * (i + 1)) // 2
    i += 1
    
tritotals = 0
for score in wordscores:
    if score in trilist:
        tritotals += 1