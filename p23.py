#!/usr/bin/env python
"""
Problem 23
02 August 2002

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

http://projecteuler.net/problem=23
"""

def divisors(n):
    for x in xrange(1, int(n**0.5) + 1):
        if n % x == 0:
            yield x
            if x > 1 and n / x != x:
                yield n / x

if __name__ == '__main__':
    abundant_numbers = []
    for x in xrange(1, 28124):
        #print x, sum(divisors(x))
        if sum(divisors(x)) > x:
            abundant_numbers.append(x)
            #print x
    abundant_sums = set()
    for x in abundant_numbers:
        for y in abundant_numbers:
            if x + y > 28123:
                break
            abundant_sums.add(x + y)
            #print x, '+', y, '=', x + y
    total = 0
    for x in xrange(1, 28124):
        if x not in abundant_sums:
            total += x
            print x
    print total
