import time 
from functools import lru_cache
from sys import stdin, stdout

# Input for this problem is to huge. 
# This code gives TLE error

@lru_cache(maxsize=8192)
def optimal_cut_cached(start, end):
  if end - start == 1:
    return 0
  min_cost = min([optimal_cut_cached(start, i) + 
                  optimal_cut_cached(i, end) for i in range(start+1, end)]) \
                  + (cuts[end] - cuts[start])
  return min_cost

sol_space = [[-1] * 52 for i in range(52)]
cuts = [0] * 52

s = time.time()
while True:
  l = int(stdin.readline().strip())
  if l == 0:
    break
  n = int(stdin.readline().strip())

  cuts = list(map(int, stdin.readline().strip().split()))
  cuts = [0] + cuts + [l]
  
  stdout.write("The minimum cutting is {}.\n".format(optimal_cut_cached(0, len(cuts)-1)))
  optimal_cut_cached.cache_clear()
  
e = time.time()
print(e - s)