"""Project Euler - Problem 14
The following iterative sequence is defined for the set of positive integers:

  n  n/2 (n is even)
  n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

  13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), it
is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def Euler014():

  # Store values and the number of steps it takes to get to 1 from that value
  steps_map = {}
  for i in range(1000000, 0, -1):
    steps = 0
    j = i
    # Store any subsequent numbers that aren't in steps_map and add later
    cache_steps = []
    while j != 1:
      # If we've already calculated the steps for a number, no need to continue
      if j in steps_map:
        steps += steps_map[j]
        break

      # Modify accordingly if a new number
      steps += 1
      if j % 2:
        j = 3*j + 1
      else:
        j = j/2
      cache_steps.append(j)

    # Get total steps
    steps_map[i] = steps

    # Add already-viewed items to cache
    if cache_steps:
      for index, num in enumerate(cache_steps):
        steps_map[num] = steps - (index + 1)


  # Print the max number of steps in steps_map
  return max(steps_map, key=lambda x: steps_map[x])


if __name__ == '__main__':
  print Euler014()
