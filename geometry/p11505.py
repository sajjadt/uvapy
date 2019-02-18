from math import sqrt
from math import sin, cos, radians
from sys import stdin, stdout

num_cases = int(stdin.readline().strip())

for c in range(num_cases):
  num_steps = int(stdin.readline().strip())
  
  x = y = 0
  forward_degree = 0

  for i in range(num_steps):
    line = stdin.readline().strip().split()
    direction, step = line[0], int(line[1])

    if direction == "fd":
      x += step*cos(radians(forward_degree))
      y += step*sin(radians(forward_degree))
    elif direction == "bc" or direction == "bk":
      x -= step*cos(radians(forward_degree))
      y -= step*sin(radians(forward_degree))
    elif direction == "lt" or direction == "lf":
      forward_degree += step
    elif direction == "rt":
      forward_degree -= step
    
  stdout.write("{}\n".format(round(sqrt(x*x + y*y))))
    