# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:34:48 2018

@author: vcian
"""

"""Each character on a computer is assigned a unique code and the preferred standard
is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then
XOR each byte with a given value, taken from a secret key. The advantage with the XOR
function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and
the key is made up of random bytes. The user would keep the encrypted message and the
encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use
a password as a key. If the password is shorter than the message, which is likely, the key
is repeated cyclically throughout the message. The balance for this method is using a sufficiently
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt the message and find the
sum of the ASCII values in the original text."""

# Notes:
# ^ is binary XOR operator
# chr() and ord() switch between ASCII and integers

# approximate frequency ranking of letters in english: _et*aoinshr
# ~%frequency: 12,12,9,9,8

# ord(' ') = 32
# lower case letters: range(97,123)
# upper case letters: range(65,91)

from string import ascii_letters,ascii_lowercase

ascii_letters += ' '

if not 'cipher' in dir():
    file = open('.spyder-py3/p059_cipher.txt')
    cipher = file.read()
    file.close()
    temp = cipher.split(',')
    
    #fix weird formatting thing
    temp[-1] = '73'
    cipher = [int(o) for o in temp]
    del temp
    
def encode(plain,key):
    cipher = []
    key = [ord(char) for char in key]
    for i,char in enumerate(plain):
        cipher.append(ord(char) ^ key[i % len(key)])
    return cipher

def decode(cipher,key):
    plain = []
    key = [ord(char) for char in key]
    for i,v in enumerate(cipher):
        j = i % len(key)
        plain.append(chr(v ^ key[j]))
    return plain
                
def letter_count(cipher,kchar):
    temp = {pos:dict.fromkeys(ascii_letters,0) for pos in range(3)}
    for pos in temp:
        temp[pos][' '] = 0
        temp[pos]['other'] = 0
    plain = decode(cipher,kchar*3)
    for i,char in list(enumerate(plain)):
        if char in ascii_letters:
            temp[i % 3][char] += 1
        else:
            temp[i % 3]['other'] += 1
    return temp

def refresh():    
    count_dict = {}
    for kchar in ascii_lowercase:
        count_dict[kchar] = letter_count(cipher,kchar)
    return count_dict

if not 'count_dict' in dir():
    count_dict = refresh()

#key_dict = {}
#for kord in range(97,123):
#    temp = [dict.fromkeys(ascii_letters,0)]*3
#    for d in temp:
#        d[' '] = 0
#        d['other'] = 0
#    plain = enumerate(decode(cipher,chr(kord)*3))
#    for i,char in enumerate(plain):
#        if char in ascii_letters:
#            temp[i % 3][char] += 1
#        else:
#            temp[i % 3]['other'] += 1
#    key_dict[chr(kord)] = temp
#    
        
def clear_candidates_low(pchar,rate):
    for kchar in count_dict:
        for pos in range(3):
            if pos in count_dict[kchar]:
                if count_dict[kchar][pos][pchar] / 400 < rate:
                    del count_dict[kchar][pos]
    sweep()

def clear_candidates_high(pchar,rate):
    for kchar in count_dict:
        for pos in range(3):
            if pos in count_dict[kchar]:
                if count_dict[kchar][pos][pchar] / 400 > rate:
                    del count_dict[kchar][pos]
    sweep()

def sweep():
    keys = tuple(count_dict.keys())
    for kchar in keys:
        if not count_dict[kchar]:
            del count_dict[kchar]
