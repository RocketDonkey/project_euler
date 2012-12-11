"""Project Euler - Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
     10: 1,2,5,10
     15: 1,3,5,15
     21: 1,3,7,21
     28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


import math
import sys

from collections import defaultdict

from primes import primes


def NumFactors(number):
  d = defaultdict(int)
  for p in ps:
    if p > number / 2:
      break

    if not number % p:
      d[p] += 1
      q = number // p
      while not q % p and q > 1:
        d[p] += 1
        q = q // p

  # Count factors
  return reduce(lambda x, y: x * (y+1), d.values(), 1)


def Euler012():
  # Grab 1000 primes
  global ps
  ps = primes.Eratosthenes(100000)[:1000]

  for i in xrange(10000, 80000):
    # Since the triangle numbers are in order, use n(n+1)/2
    num = (i*(i+1))/2
    if NumFactors(num) > 500:
      return num


if __name__ == '__main__':
  print Euler012()