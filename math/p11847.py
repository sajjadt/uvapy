
from sys import stdin, stdout
from math import log2

while True:
  n = int(stdin.readline().strip())
  if n == 0:
    break

  # Optial cutting would be different pieces of 2^i length
  stdout.write("{}\n".format(int(log2(n))))
