#!/usr/bin/env python
"""
Problem 26
13 September 2002

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

http://projecteuler.net/problem=26
"""

from decimal import *

def find_recurring(d):
    s = str(d).replace('.', '')
    r = 0
    for x in xrange(len(s), 0, -1):
        if s[-x:] == s[-2*x:-x]:
            r = x
    if not r:
        return ''
    for x in xrange(0, len(s)):
        if s[x:x+r] == s[x+r:x+2*r]:
            return s[x:x+r]

if __name__ == '__main__':
    getcontext().prec = 10000
    getcontext().rounding = ROUND_DOWN
    d = 0
    max_r = ''
    for x in xrange(1, 1001):
        #print x, Decimal(1.0) / Decimal(x), find_recurring(Decimal(1.0) / Decimal(x))
        r = find_recurring(Decimal(1.0) / Decimal(x))
        if len(r) > len(max_r):
            d = x
            max_r = r
    print d, max_r, len(max_r)
