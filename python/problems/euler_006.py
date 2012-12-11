"""Project Euler - Problem 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def Euler006():
  n = 100

  # Square of sums
  square_of_sum = ((n*(n+1))/2)**2

  # Sum of squares is pyramidal, so we can plug in our n
  # and get the sum of the first n numbers
  sum_of_squares = (2*(n**3) + 3*(n**2) + n)/6

  return square_of_sum - sum_of_squares


def main():
  print Euler006()


if __name__ == '__main__':
  main()
