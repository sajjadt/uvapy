from math import isclose, sqrt, atan2, degrees, sin, cos, pi

def error(message):
  raise ValueError(message)

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, point):
    return sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2))
  
  def __str__(self):
    return str((self.x, self.y))

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def rotate(self, radians):
    COS = cos(radians)
    SIN = sin(radians)
    x = COS*self.x-SIN*self.y
    y = SIN*self.x+COS*self.y
    self.x = x
    self.y = y

  def __str__(self):
    return "({}, {})".format(self.x, self.y)

class Circle:
  def __init__(self, **kwargs):
    if "p1" in kwargs and "p2" in kwargs and "p3" in kwargs:
      self.from_three_points(kwargs["p1"], kwargs["p2"],  kwargs["p3"])
    elif "c" in kwargs and "r" in kwargs:
      self.from_center_radius(kwargs["c"], kwargs["r"])
    else:
      error("Unknown constructor called: {}".format(kwargs.keys()))

  def from_center_radius(self, c, r):
    self.c = c
    self.r = r
  
  def from_three_points(self, p1, p2, p3):

    if isclose(p1.x, p2.x):
      p3, p1= p1, p3
    mr = (p2.y-p1.y) / (p2.x-p1.x)
    if isclose(p2.x, p3.x):
      p1, p2= p2, p1
    mt = (p3.y-p2.y) / (p3.x-p2.x)

    if isclose(mr, mt):
      error("No such circle exists.")
  
    x = (mr*mt*(p3.y-p1.y) + mr*(p2.x+p3.x) - mt*(p1.x+p2.x)) / (2*(mr-mt))
    y = (p1.y+p2.y)/2 - (x - (p1.x+p2.x)/2) / mr
    radius = sqrt((pow((p2.x-x), 2) +  pow((p2.y-y), 2)))

    self.c = Point2D(x, y)
    self.r = radius

  def __str__(self):
    return "C:{}, R:{}".format(self.c, self.r)

test_no = 1
while True:
  n = int(input())

  if n == 0:
    break

  line = input().split()
  p1 = Point2D(float(line[0]), float(line[1]))
  line = input().split()
  p2 = Point2D(float(line[0]), float(line[1]))
  line = input().split()
  p3 = Point2D(float(line[0]), float(line[1]))
  
  c = Circle(p1=p1, p2=p2, p3=p3)

  # This case is the same as the bounding box 
  #   -----
  #  |     |    
  #  |     |
  #   -----
  # find the min x,y for all the points on polygon
  x_min = x_max = p1.x
  y_min = y_max = p1.y

  v = Vector2D(p1.x-c.c.x, p1.y-c.c.y)

  rotation_degree = 2*pi/n
  for i in range(n-1):
    v.rotate(rotation_degree)
    x_min = min(v.x+c.c.x, x_min)
    y_min = min(v.y+c.c.y, y_min)
    x_max = max(v.x+c.c.x, x_max)
    y_max = max(v.y+c.c.y, y_max)

  print("Polygon {}: {:.3f}".format(test_no, (x_max-x_min)*(y_max-y_min)))
  test_no += 1  