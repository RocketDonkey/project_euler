"""Project Euler - Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each
of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def Factor(n):
  i = n / 2
  k = 2
  factors = []
  while k <= i:
    if not n % k:
      factors.append(k)
    k += 1
  return sum([1] + factors)

def Euler021():
  amic_map = {}
  for i in range(1, 10000):
    amic_map[i] = Factor(i)

  summer = 0
  for num, val in amic_map.iteritems():
    comp = amic_map.get(val, None)
    if comp == num and val != comp:
      summer += num

  return summer


if __name__ == '__main__':
  print Euler021()
