from sys import stdin, stdout
from time import time

# This code  receives TLE error..
# t1 = time()
# data = stdin.readlines()
# lc = 0
# out = []

# while lc < len(data):
#   x = int(data[lc].strip())
#   res = 0
#   y = 1
#   for i, c in enumerate(reversed(data[lc+1].strip().split())):
#     if i > 0:
#       res += int(c)*i*y
#       y = y*x
#   out.append(res)
#   lc += 2

# t2 = time()
# stdout.write("{}\n".format("\n".join(map(str, out))))
# print(t2-t1)


# Optimized with Horner's rule
t1 = time()
data = stdin.readlines()
lc = 0
out = []

while lc < len(data):
  x = int(data[lc].strip())
  res = 0
  coeffs = data[lc+1].strip().split()
  n = len(coeffs) - 1 
  for i, c in enumerate(coeffs):
    if i < n:
      res = x * res
      res += int(c)*(n-i)
  out.append(res)
  lc += 2

t2 = time()
stdout.write("{}\n".format("\n".join(map(str, out))))
# print(t2-t1)