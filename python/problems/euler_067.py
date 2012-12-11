"""Project Euler - Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

"""

def Collapse(l):
  prev = l[-1]
  # Row of the triangle
  for row_num, i in enumerate(reversed(l[:-1])):
    collapse = []

    # This is the row itself
    for index, j in enumerate(i):
      maxes = [j + prev[index+q] for q in range(2)]
      collapse.append(max(maxes))
    prev = collapse
  return collapse


def Euler067():

  with open('./data/triangle.txt', 'rb') as f:
    contents = [[int(i) for i in l.split()] for l in f.readlines()]

  # Collapse the triangle into its nodes and take the max
  return max(Collapse(contents))

if __name__ == '__main__':
  print Euler067()
