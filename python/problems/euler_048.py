"""Project Euler - Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def Euler048():
  return str(sum(i**i for i in xrange(1, 1001)))[-10:]


if __name__ == '__main__':
  print Euler048()
