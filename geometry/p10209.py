from math import sqrt
from math import pi
from sys import stdin, stdout



factor = sqrt(3)/2
while True:
  try:
    dim = float(input())
    dim_2 = dim*dim
    h = dim * factor
    
    # c is the area of each region formed by square edges (grid highlight)
    # a is area of region in the center (stripe highlight)
    
    c = dim*(dim - h) - ( (1/6)*(pi*dim_2) - (h*dim)/2)
    b = dim_2 - (pi/4)*dim_2 - 2*c

    total_c = 4*c
    total_b = 4*b
    
    total_a = dim_2 - total_b - total_c
    stdout.write("{:.3f} {:.3f} {:.3f}\n".format(total_a, total_b, total_c)) 

  except(EOFError):
    break