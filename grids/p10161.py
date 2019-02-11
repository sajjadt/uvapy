from sys import stdin, stdout
from math import sqrt

while True:
  n = int(stdin.readline().strip())
  if n == 0:
    break
  
  root = int(sqrt(n))
  diff = n - root*root
  
  r = c = 0
  
  if diff == 0:
    if root & 1 == 1:
      row, col = root, 1
    else:
      row, col = 1, root
  else:
    if root & 1 == 1:
      # -
      if diff <= root + 1:
        row, col = root + 1, diff
      else:
        row, col = (root+1)**2 - n + 1, root + 1
    else:
      #  |
      if diff <= root + 1:
        row, col = diff, root + 1
      else:
        row, col = root + 1, (root+1)**2 - n + 1

  stdout.write("{} {}\n".format(col, row))


