#!/usr/bin/env python
"""
Problem 22
19 July 2002

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

http://projecteuler.net/problem=22
"""

def word_score(s):
    return sum([ord(c) - 96 for c in s.lower()])

if __name__ == '__main__':
    print word_score('COLIN'), '(==53)'
    names = [x.strip('"').lower() for x in file('names.txt').read().split(',')]
    names.sort()
    print names.index('colin') + 1, '(==938)'
    print sum([(n + 1) * word_score(s) for n, s in enumerate(names)])
