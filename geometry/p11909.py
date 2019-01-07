from math import tan, acos

pi = acos(-1)

def to_radian(degrees):
  degrees = degrees % 360
  return (pi * degrees) / 180

while True:
  try:
    l, w, h, theta = list(map(int, input().split()))

    # convert to radians
    theta = to_radian(theta)
    h_prim = l* tan(theta) 

    if h_prim <= h:
      # calc overflow amount and subtract from bottle volume
      volume = w * l * (h - h_prim /2)  
    else:
      # calc what is left in the bottle directly
      volume = w * h * h * (1 / tan(theta)) / 2
    
    print("{:0.3f} mL".format(max(volume, 0)))
  except(EOFError):
    break