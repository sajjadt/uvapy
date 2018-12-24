#!/usr/bin/python3
from math import factorial

while True:
  try:
    line = input()
    n, k = list(map(int, line.split()))
    line = list(map(int, input().split()))

    # Solution = n!/ (n1! n2! n3! ... nk!)
    solution = factorial(n)
    for nk in line:
      solution /= factorial(nk) 
    
    print(int(solution))
  
  except EOFError:
    break

