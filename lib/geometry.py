from math import atan, pi, pow, sqrt

def to_radian(degrees):
  degrees = degrees % 360
  return (pi * degrees) / 180

def distance_l2(p1, p2):
  return pow(p2[0]-p1[0], 2) + pow(p2[1] - p1[1], 2)

def distance(p1, p2):
  return sqrt(pow(p2[0]-p1[0], 2) + pow(p2[1] - p1[1], 2))


