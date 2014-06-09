#!/usr/bin/env python
"""
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.

http://projecteuler.net/index.php?section=problems&id=4
"""

def largest_palindrome(digits):
    nmax = 10**digits - 1 
    nmin = 10**digits / 10
    palindromes = set()
    for x in xrange(nmax, nmin, -1):
        for y in xrange(x, nmin, -1):
            z = x * y
            if str(z) == ''.join(reversed(str(z))):
                palindromes.add((z, x, y))
    if palindromes:
        return sorted(palindromes, key=lambda x: x[0], reverse=True)[0]

if __name__ == '__main__':
    result = largest_palindrome(3)
    print 'Largest palindrome as product of 3-digit numbers is', result[0],
    print '(', result[1], '*', result[2], ')'
