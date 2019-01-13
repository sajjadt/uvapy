# Diagonal - UVA 10784 

import cmath
from math import ceil

def solve_quadratic(a, b, c):
  delta = (b**2) - (4*a*c)

  sol1 = (-b-cmath.sqrt(delta))/(2*a)
  sol2 = (-b+cmath.sqrt(delta))/(2*a)

  return sol1, sol2

case_no = 1
while True:
  num = int(input())
  if num == 0:
    break
  
  sol1, sol2 = solve_quadratic(1, -3, -2*num)
  print("Case {}: {}".format(case_no, ceil(sol2.real)))

  case_no += 1
