#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problem 31
22 November 2002

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1 £1 + 1 50p + 2 20p + 1 5p + 1 2p + 3 1p

How many different ways can £2 be made using any number of coins?

http://projecteuler.net/problem=31
"""

coins = {
    1: '1p',
    2: '2p',
    5: '5p',
    10: '10p',
    20: '20p',
    50: '50p',
    100: '£1',
    200: '£2',
}

def combinations(elements):
    if elements:
        for x in xrange(0, 200 / elements[0] + 1):
            for other in combinations(elements[1:]):
                result = [(elements[0], x)] + other
                result = [(a, b) for a,b in result if b]
                yield result
    yield []

def attempt1():
    cs = set()
    for c in combinations(sorted(coins.keys(), reverse=True)):
        s = sum([a*b for a,b in c])
        if s == 200 and c not in cs:
            cs.add(c)
            print c

def remainder(r, opts):
    for n, o in enumerate(opts):
        for x in xrange(1, r / o + 1):
            r2 = r - (o * x)
            #print o, x, r, r2
            if r2 > 0:
                for res in remainder(r2, opts[n+1:]):
                    yield [(o, x)] + res
            elif r2 == 0:
                yield [(o, x)]
            else:
                continue

if __name__ == '__main__':
    n = -1
    for n, res in enumerate(remainder(200, sorted(coins.keys()))):
        print n, res
    print n + 1
