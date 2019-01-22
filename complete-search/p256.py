from math import sqrt
import cmath
from sys import stdout

def solve_quadratic(a, b, c):
  delta = (b**2) - (4*a*c)
  sol1 = (-b-cmath.sqrt(delta))/(2*a)
  sol2 = (-b+cmath.sqrt(delta))/(2*a)
  return sol1, sol2

# Preprocess Results
# X.Y
# X * 10^d + Y = (X + Y)^2
# X * 10^d + Y - X^2 - Y^2 - 2xy = 0
# Y^2 + Y(2x-1) + X^2-10^d*x = 0
result = []
for d in range(1, 5):
  limit = 10**d
  result.append([])
  for x in range(limit):
    sol1, sol2 = solve_quadratic(1, 2*x-1, x*x-limit*x)
    if sol1.imag == 0 and sol1.real >=0 and sol1.real < limit and sol1.real == int(sol1.real):
      result[-1].append(str(x).zfill(d)+str(int(sol1.real)).zfill(d))
    if sol2.imag == 0 and sol2.real >=0 and sol2.real < limit and sol2.real == int(sol2.real):
      result[-1].append(str(x).zfill(d)+str(int(sol2.real)).zfill(d))

while True:
  try:
    n = int(input())
    stdout.write("\n".join(result[n//2-1])+"\n")

  except(EOFError):
    break