#!/usr/bin/env python
"""
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is:

   1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

   (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

http://projecteuler.net/index.php?section=problems&id=6
"""

def sum_of_squares(numbers):
    return sum(map(lambda x: x**2, numbers))

def square_of_sums(numbers):
    return sum(numbers)**2

def diff_between(numbers):
    return square_of_sums(numbers) - sum_of_squares(numbers)

if __name__ == '__main__':
    print diff_between(range(1, 11, 1))
    print diff_between(range(1, 101, 1))
