from math import sqrt

while True:
  try:
    l, w = list(map(float, input().split()))

    # V(x) = x (L - 2x) (W - 2x)
    # dV/dx = 12x * x - 4(L+W) * x + w * l
     
    # Solve quadratic equation ax**2 + bx + c = 0
    a = 12
    b = -4 * (l+w)
    c = w*l
    delta = (b**2) - (4*a*c)
    sol1 = (-b-sqrt(delta))/(2*a)
    sol2 = (-b+sqrt(delta))/(2*a)
    
    if sol1 < min(w, l) / 2:
      x_max = sol1
    else:
      x_max = sol2

    # trick to round up the number
    x_min = min(l, w)/2 + 0.00000001
    
    print("{:.3f} 0.000 {:.3f}".format(x_max, x_min))
  except(EOFError):
    break