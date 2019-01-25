from functools import lru_cache
from operator import getitem

LIMIT = 10000 + 1
pow_table = [1]
for i in range(LIMIT):
  pow_table.append(2*pow_table[-1])

best_choice = [0, 0, 0, 1]
for disp in range(3, 150):
  b = best_choice[-1]
  for j in range(disp):
    best_choice.append(b+j)

@lru_cache(maxsize=(2**14))
def f(n):
  if n <= 1:
    return n
  
  k = best_choice[n]
  sol = 2*f(k) + 2**(n-k) - 1
  return sol

while True:
  try:
    inp = int(input())
    print(f(inp))
  except(EOFError):
    break