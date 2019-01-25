from math import isclose

class Circle:
  def __init__(self, **kwargs):
    if "p1" in kwargs and "p2" in kwargs and "p3" in kwargs:
      self.from_three_points(kwargs["p1"], kwargs["p2"],  kwargs["p3"])
    # elif "c" in kwargs and "r" in kwargs:
    #   self.from_center_radius(kwargs["c"], kwargs["r"])
    else:
      raise ValueError("Unknown constructor called: {}".format(kwargs.keys()))

  def from_three_points(self, p1, p2, p3):
    
    if isclose(p1.x, p2.x):
      p3, p1= p1, p3
    mr = (p2.y-p1.y) / (p2.x-p1.x)
    if isclose(p2.x, p3.x):
      p1, p2= p2, p1
    mt = (p3.y-p2.y) / (p3.x-p2.x)

    if isclose(mr, mt):
      raise ValueError("No such circle exists.")
  
    x = (mr*mt*(p3.y-p1.y) + mr*(p2.x+p3.x) - mt*(p1.x+p2.x)) / (2*(mr-mt))
    y = (p1.y+p2.y)/2 - (x - (p1.x+p2.x)/2) / mr
    radius = pow((pow((p2.x-x), 2) +  pow((p2.y-y), 2)), 0.5)

    self.c = (x, y)
    self.r = radius

while True:
  n = int(input())
  if n == 0:
    break
  
  points = []
  for i in range(n):
    p = tuple(map(int, input().split()))
    points.append(p)
  r = float(input())
  if n == 1:
    # Always feasible to embed a point in a circle (r == 0?)
    print("The polygon can be packed in the circle.")
  elif n == 2:
    dist_l2 = (points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1])**2
    if dist_l2 <= (r+r)**2:
      print("The polygon can be packed in the circle.")
    else:
      print("There is no way of packing that polygon.")
  else:
    # Find a circle that passes through first three points
    c = Circle(p1 = points[0], p2 = points[1], p3 = points[2])