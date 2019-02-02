from math import sqrt

num_tests = int(input())

for t in range(num_tests):
  num_points = int(input())
  points = []
  for i in range(num_points):
    points.append(list(map(int, input().split())))
  points.sort()

  # Keep track of max height seen
  sunny_len = 0
  hmax = 0
  for i in range(len(points)-2, -1, -1):
    if points[i][1] > hmax:
      # add to sunny len

      dist = sqrt(  (points[i][0] - points[i+1][0])**2  +(points[i][1] - points[i+1][1])**2 )
      side =  dist * (points[i][1] - hmax)  / (points[i][1] - points[i+1][1])

      sunny_len += side
      hmax = points[i][1]

  print("{:.2f}".format(sunny_len))
