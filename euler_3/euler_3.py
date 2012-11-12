"""Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def Eratosthenes(n):

  # Skip all multiples of two since they won't count
  numlist = range(3, n+1, 2)
  # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

  # In numlist, toggle non-primes to 0
  backup = 0
  for num in numlist:
    counter = backup
    if num:
      counter += num
      while counter <= len(numlist)-1:
        numlist[counter] = 0
        counter += num
    backup += 1
  return filter(bool, numlist)

def main():
  start = 600851475143
  num = int(math.sqrt(start))
  l = Eratosthenes(num)

  for prime in reversed(l):
    if not start % prime:
      print 'Num {0} % {1} = {2}'.format(start, prime, start % prime)
      break


if __name__ == '__main__':
  main()
