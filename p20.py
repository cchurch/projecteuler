#!/usr/bin/env python
"""
Problem 20
21 June 2002

n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

http://projecteuler.net/problem=20
"""

import math

def sum_of_digits(n):
    t = 0
    while n:
        t += n % 10
        n /= 10
    return t

if __name__ == '__main__':
    print sum_of_digits(math.factorial(10)), '10! -> 27'
    print sum_of_digits(math.factorial(100)), '100! -> ??'
