# Thrash Removal
from operator import getitem
from math import sqrt, isclose
from time import time
from sys import stdin

def convex_hull(points):

  points.sort()

  if len(points) <= 1:
    return points
  
  def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

  # Build lower hull 
  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
      lower.pop()
    lower.append(p)

  # Build upper hull
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)

  # Concatenation of the lower and upper hulls gives the convex hull.
  # Last point of each list is omitted because it is repeated at the beginning of the other list. 
  return lower[:-1] + upper[:-1]

s = time()
test = 1
while True:
  n = int(input())
  if n == 0:
    break
  
  points = []
  for i in range(n):
    p = tuple(map(int, stdin.readline().strip().split()))
    points.append(p)
  
  
  # 100 points, even less in the convex, o(n^2) solution is reasonable
  points = convex_hull(points)

  n = len(points)  # size of polygon has changed
  points.append(points[0])
  
  min_dist = 10**16
  for i in range(1, len(points)):
    
    p1=points[i-1]
    p2=points[i]
    
    # (Line from two points) Inlined function for performance
    if isclose(p1[0], p2[0]):
      l_a = 1
      l_b = 0
      l_c = -p1[0]
    else:
      m = -(p2[1] - p1[1]) / (p2[0] - p1[0])
      l_a = m
      l_b = 1
      l_c = -m*p1[0]-p1[1]

    max_dist = 0
    for j in range(0, len(points)-1):
      if j == i or j == i-1 or i == j + n:
        continue

      # Point-line distance
      dist = abs(l_a * points[j][0] + l_b * points[j][1] + l_c) / sqrt(l_a * l_a + l_b * l_b)

      if dist > max_dist:
        max_dist = dist
    if max_dist < min_dist:
      min_dist = max_dist
  print("Case {}: {:.2f}".format(test, min_dist))
  test += 1
e = time()
# print(e-s)

