"""Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

from primes import primes


def Euler003():
  start = 600851475143
  num = int(math.sqrt(start))
  l = primes.Eratosthenes(num)

  for prime in reversed(l):
    if not start % prime:
      return prime


def main():
  Euler003()

if __name__ == '__main__':
  main()
