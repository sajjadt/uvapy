from math import pi

# Cone volume = 1/3 pi r**2 h (r = radius, h = height)

while True:
  D, V = list(map(int, input().split()))

  if D == V == 0:
    break

  # After consdiering paritial cones and inner cylender area and some simplifications
  d = pow(D**3 - 6*V/pi, 1/3)

  print("{:.3f}".format(d))