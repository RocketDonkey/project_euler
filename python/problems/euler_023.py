"""Project Euler - Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

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
"""


from itertools import combinations_with_replacement as cwr


def Factor(n):
  i = n / 2
  k = 2
  factors = []
  while k <= i:
    if not n % k:
      factors.append(k)
    k += 1
  return sum([1] + factors)

def Euler023():
  amic_map = {}
  for i in range(12, 28124):
    f = Factor(i)
    if f > i:
      amic_map[i] = f

  nums = set([x for x in (sum(i) for i in cwr(amic_map, 2)) if x < 28124])
  return sum(set(range(1, 28124)) - nums)


if __name__ == '__main__':
  print Euler023()
