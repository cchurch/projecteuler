#!/usr/bin/env python
"""
Problem 16
03 May 2002

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

http://projecteuler.net/problem=16
"""

def sum_of_digits(n):
    t = 0
    while n:
        t += n % 10
        n /= 10
    return t

if __name__ == '__main__':
    print sum_of_digits(2**15), '(==26)'
    print sum_of_digits(2**1000), '(==???)'
