from math import sqrt, pi
while True:
  try:
    a, b, c = list(map(int, input().split()))

    s = (a + b + c ) /2
    tri_area = sqrt(s * (s - a) * (s -b) * (s - c))
    r_inner = tri_area / s
    inner_c_area = r_inner*r_inner*pi
    r_outer = a*b*c/(4*tri_area)  # proof by triangle simliarity 
    outer_c_area = r_outer*r_outer*pi
    print("{:.4f} {:.4f} {:.4f}".format(outer_c_area-tri_area, tri_area-inner_c_area, inner_c_area))
  except(EOFError):
    break