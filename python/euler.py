"""Project Euler - Python solutions.

(Very) basic solutions in Python. Apparently I'm not good at algorithms??
"""

import sys

# Allow problem modules to import utility modules
sys.path.append('.')

from problems import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    RED = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def main():
  print '*****************************'
  print '** Project Euler in Python **'
  print '*****************************'

  for i in range(1, 70):
    m = 'euler_{0:03d}'.format(i)
    f = 'Euler{0:03d}'.format(i)
    try:
      print (bcolors.OKBLUE +
             '{2}Problem {0}:{4} {3}{1}{4}'.format(
                 i, getattr(globals()[m], f)(),
                 bcolors.OKBLUE, bcolors.OKGREEN, bcolors.ENDC)
             )
    except KeyError:
      print '{1}Problem {0}:{3} {2}UNSOLVED{3}'.format(
          i, bcolors.OKBLUE, bcolors.FAIL, bcolors.ENDC)


if __name__ == '__main__':
  main()
