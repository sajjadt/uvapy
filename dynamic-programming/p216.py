import math
from functools import lru_cache

Inf = 1000000

cart_dist = lambda p1, p2: 0 if (p1 == None or p2 == None) else math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
  
def min_line(points, visited):
  ''' points: set of tuples(x, y) '''
  # Represent visited boolean vector as a boolean vector (integer or string)
  @lru_cache(maxsize=(2**12))
  def min_line_recursive(start, visited):
    if ~ visited == 0:
      return 0, []

    min_val = Inf
    min_ind = -1
    for i in range(len(points)):
      if visited & (1 << i) == 0 :
        visited = visited ^ (1 << i)
        ret_val = min_line_recursive(points[i], visited)
        cur_val = cart_dist(start, points[i]) + ret_val[0]
        if cur_val < min_val:
          min_val = cur_val
          min_ind = [i] + ret_val[1]
        visited = visited & (~ (1 << i))
    
    return min_val, min_ind 

  return min_line_recursive(None, visited)

test_no = 1
while True:
  num_points = int(input())
  
  if num_points == 0:
    break

  points = []
  for i in range(num_points):
    points.append(tuple(map(int, input().split())))
  
  visited = ~ ((2**(num_points)) - 1)
  ret = min_line(points, visited)
  print("**********************************************************")
  print("Network #{}".format(test_no))

  path = ret[1]
  for i in range(num_points-1):
    print("Cable requirement to connect ({},{}) to ({},{}) is {:.2f} feet.".format( *points[path[i]], *points[path[i+1]], 16+ cart_dist(points[path[i]], points[path[i+1]])))
  print("Number of feet of cable required is {:.2f}.".format(ret[0]+ (16)*(num_points-1)))

  test_no += 1