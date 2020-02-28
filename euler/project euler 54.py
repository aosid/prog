# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:31:04 2018

@author: vcian
"""

"""In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example,
a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example,
both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
                     	2C 3S 8S 8D TD
                         Pair of Eights
                                             Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
                                         	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
     
The file, p054_poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space):
    the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?"""

file = open("C:\\Users\\vcian\\.spyder-py3\\p054_poker.txt")
hands = file.read().split("\n")
file.close()

faces = dict(zip(['T','J','Q','K','A'],range(10,15)))

# Returns a list containing values [0] and suits [1]
def parse_hand(hand):
    global faces
    clist = [[],[]]
    for card in hand:
        if card[0] in faces:
            clist[0].append(faces[card[0]])
        else:
            clist[0].append(int(card[0]))     
        clist[1].append(card[1])
    return clist

def isStraight(hand):
    start = min(hand[0])
    for i in range(1,5):
        if (start + i) not in hand[0]:
            return False
    return True

def isFlush(hand):
    if len(set(hand[1])) == 1:
        return True
    return False

def count(hand):
    vdict = {}
    for val in hand[0]:
        if val not in vdict:
            vdict[val] = 0
        vdict[val] += 1
    return vdict

def rank(hand):
    values = list(hand[0])
    values.sort()
    values.reverse()
    if (isStraight(hand) and isFlush(hand)):
        return (0,values)
    if isFlush(hand):
        return (3,values)
    if isStraight(hand):
        return (4,values)
    temp = count(hand)
    rcounts = {v:k for k,v in temp.items()}
    counts = list(temp.values())
    counts.sort()
    if counts[1] == 4:
        return (1,(rcounts[4]))
    if counts == [2,3]:
        return (2,(rcounts[3],rcounts[2]))
    if counts[-1] == 3:
        for i in range(3):
            values.remove(rcounts[3])
        return (5,(rcounts[3],values[0],values[1]))
    if counts == [1,2,2]:
        h = values[3]
        l = values[1]
        for i in range(2):
            values.remove(l)
            values.remove(h)
        return (6,(h,l,values[0]))
    if counts[-1] == 2:
        for i in range(2):
            values.remove(rcounts[2])
        return (7,(rcounts[2],values[0],values[1],values[2]))
    return (8,values)

def compare_hands(line):
    hands = line.split()
    if len(hands) != 10:
        return
    hand1 = parse_hand(hands[:5])
    hand2 = parse_hand(hands[5:])
    ranks = (rank(hand1),rank(hand2))
    if ranks[0][0] != ranks[1][0]:
        return ranks.index(min(ranks))
    for i in range(5):
        if ranks[0][1][i] != ranks[1][1][i]:
            if ranks[0][1][i] > ranks[1][1][i]:
                return 0
            return 1
        
total1 = 0
total2 = 0
for hand in hands[:-1]:
    if not compare_hands(hand):
        total1 += 1
    else:
        total2 += 1