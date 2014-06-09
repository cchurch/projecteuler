#!/usr/bin/env python
"""
Problem 30
08 November 2002

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

http://projecteuler.net/problem=30
"""

def sum_of_power_of_digits(n, p):
    digits = [int(c) for c in str(n)]
    return sum([d**p for d in digits])

def sum_of_numbers(p):
    z = 0
    for x in xrange(2, 1000000):
        s = sum_of_power_of_digits(x, p)
        if x == s:
            z += x
            digits = [int(c) for c in str(x)]
            print x, '=', ' + '.join(['%d^%d' % (d, p) for d in digits])
    return z

if __name__ == '__main__':
    s = sum_of_numbers(4)
    print 'sum(4) =', s
    s = sum_of_numbers(5)
    print 'sum(5) =', s
