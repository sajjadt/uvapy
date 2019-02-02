import math
from functools import lru_cache

Inf = 100

dist = lambda p1, p2: 0 if (p1 == None or p2 == None) else abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
  
def minimal_cycle(start, points, visited):
  ''' points: set of tuples(x, y) '''
  # Represent visited boolean vector as a boolean vector (integer or string)
  @lru_cache(maxsize=(2**14))
  def min_cycle_recursive(current, visited):
    if ~ visited == 0:
      return dist(start, current)
    min_val = Inf
    for i in range(len(points)):
      if visited & (1 << i) == 0 :
        visited = visited ^ (1 << i)
        ret_val = min_cycle_recursive(points[i], visited)
        cur_val = dist(current, points[i]) + ret_val
        if cur_val < min_val:
          min_val = cur_val
        visited = visited & (~ (1 << i))
    
    return min_val
  
  visited = visited & (~1)
  return min_cycle_recursive(points[0], visited)


from time import time
from sys import stdin, stdout

st = time()
num_cases = int(stdin.readline().strip())
for t in range(num_cases):
  w, h = list(map(int, stdin.readline().strip().split()))
  start = tuple(map(int, stdin.readline().strip().split()))

  num_points = int(stdin.readline().strip())
  points = [start]
  for i in range(num_points):
    points.append(tuple(map(int, stdin.readline().strip().split())))
  
  visited = ~ ((2**(num_points+1)) - 1)
  ret = minimal_cycle(start, points, visited)
  
  stdout.write("The shortest path has length {}\n".format(ret))

et = time()
# print(et - st)