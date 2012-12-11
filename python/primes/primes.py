"""Project Euler - Primes

Functions for dealing with primes.
"""

def Eratosthenes(n):
  """ Return the first n primes."""

  # Skip all multiples of two since they won't count
  numlist = range(3, n+1, 2)

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
  return [2] + [x for x in numlist if x]
