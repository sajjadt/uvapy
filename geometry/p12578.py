from math import acos

pi = acos(-1)
num_tests = int(input())

for i in range(num_tests):
  l = int(input())
  h = 0.6 * l 
  r = 0.2 * l
  total_area = l * h
  red_area = pi * r * r
  print("{:.2f} {:.2f}".format(red_area, total_area - red_area))
