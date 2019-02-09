from math import sqrt
from sys import stdin, stdout

num_cases = int(stdin.readline().strip())

for c in range(num_cases):
  f, t = list(map(int, stdin.readline().strip().split()))

  diff = t - f

  if diff == 0:
    res = 0
  else:
    n = int(sqrt(diff))
    k = diff - (n*n)
    res = 2*n - 1 
    if k > 0:
      res += 1
    if k > n:
      res += 1

  stdout.write("{}\n".format(res))

