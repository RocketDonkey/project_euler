"""Project Euler - Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


from itertools import combinations

def MyAnswer():
  pals = []
  for i, i2 in combinations(range(999, 100, -1), 2):
    s = str(i * i2)
    if s[:3] == s[-1::-1][:3]:
      pals.append(int(s))
  res = sorted(pals)

  return res[-1]


def main():
  print MyAnswer()


if __name__ == '__main__':
  main()
