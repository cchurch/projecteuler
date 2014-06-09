#!/usr/bin/env python
"""
Problem 24
16 August 2002

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

http://projecteuler.net/problem=24
"""

def permutations(items):
    if not items:
        yield []
    else:
        for item in items:
            new_items = [x for x in items if x != item]
            for permutation in permutations(new_items):
                yield [item] + permutation

if __name__ == '__main__':
    for p in permutations([0, 1, 2]):
        print ''.join(map(str, p))
    for n, p in enumerate(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
        if n + 1 == 1000000:
            print ''.join(map(str, p))
            break
