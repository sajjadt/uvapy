from math import sqrt
from sys import stdin, stdout

h = 0.8660254037844386
h_3 = h/3
h_23 = 2*h/3

# Top of top triangle is axis (x=0, y=0.5)
def find_center_coord(index):
  root = int(sqrt(index))

  y = -root*h
  
  if index % 2 == root % 2:
    #   .
    #  / \
    # -----
    y -= h_23
  else:
    # -----
    #  \ /
    #   .
    y -= h_3
  
  disp = index - root*root
  x = (0.5) * (disp-root)

  return x, y


while True:
  line = stdin.readline().strip()
  if line == "":
    break 
  line = line.split()
  s, t = int(line[0]), int(line[1])
  x1, y1 = find_center_coord(s)
  x2, y2 = find_center_coord(t)
  distance = sqrt((y1-y2)**2 + (x1-x2)**2)
  stdout.write("{:.3f}\n".format(distance))
