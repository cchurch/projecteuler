#!/usr/bin/env python
"""
Problem 17
17 May 2002

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

http://projecteuler.net/problem=17
"""

import string

def n2s(n):
    digits = dict(enumerate(['zero', 'one', 'two', 'three', 'four', 'five',
                             'six', 'seven', 'eight', 'nine']))
    prefixes = {2: 'twen', 3: 'thir', 4: 'for', 5: 'fif', 8: 'eigh'}
    n = int(n)
    words = []
    if n >= 1000:
        words = [n2s(n / 1000), 'thousand']
        if n % 1000:
            words.append(n2s(n % 1000))
    elif n >= 100:
        words = [n2s(n / 100), 'hundred']
        if n % 100:
            words.extend(['and', n2s(n % 100)])
    elif n >= 20:
        word = '%sty' % (prefixes.get(n / 10) or digits.get(n / 10))
        if n % 10:
            word = '%s-%s' % (word, n2s(n % 10))
        words = [word]
    elif n >= 10:
        word = {10: 'ten', 11: 'eleven', 12: 'twelve', 14: 'fourteen'}.get(n)
        if not word:
            word = '%steen' % (prefixes.get(n % 10) or digits.get(n % 10))
        words = [word]
    else:
        words = [digits.get(n)]
    return ' '.join(words)

def num_letters(s):
    return len([c for c in s if c in string.letters])

if __name__ == '__main__':
    #for x in xrange(1, 1001):
    #    print x, n2s(x), num_letters(n2s(x))
    print sum(num_letters(n2s(x)) for x in xrange(1, 6)), '(==19)'
    print sum(num_letters(n2s(x)) for x in xrange(1, 1001)), '(==??)'
