"""Project Euler - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

from primes import primes


def Euler010():
  return sum(primes.Eratosthenes(2000000))


def main():
  print Euler010()


if __name__ == '__main__':
  main()
