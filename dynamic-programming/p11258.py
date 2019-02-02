
from functools import lru_cache
import sys

MAX_INT = 2147483647
sys.setrecursionlimit(1000)

LIMIT = 200 + 1
dp_table = [0]*LIMIT

@lru_cache(maxsize=2**8)
def max_partition_1d(text):

  if len(text) == 0:
    return 0

  if len(text) < 10:
    return int(text)
  else:
    max_sol = -1
    acc_val = 0
    i = 0
    while acc_val <= MAX_INT and i < len(text):
      acc_val = acc_val * 10 + int(text[i])
      rec_sol = max_partition_1d(text[i+1:]) 
      
      if rec_sol != -1 and acc_val <= MAX_INT:
        max_sol = max(acc_val + rec_sol, max_sol)
      
      i += 1
    
    return max_sol

import time

st = time.time()
num_cases = int(input())
for case in range(num_cases):
  num = input()
  if len(num) >= 10:
    print(max_partition_1d(num))
    max_partition_1d.cache_clear()
  else:
    print(int(num))
et = time.time()
# print(et - st)