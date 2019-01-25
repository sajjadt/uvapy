while True:
  try:
    line = input().split()
    if len(line) < 8:
      break
    points = list(map(float, line))
    p_a = points[0], points[1]
    p_b = points[2], points[3]
    p_x = points[4], points[5]
    p_y = points[6], points[7]
    if p_x == p_b:
      p_c = p_y
    elif p_y == p_b:
      p_c = p_x
    elif p_x == p_a:
      p_c = p_y
      p_a, p_b = p_b, p_a
    else:
      p_c = p_x
      p_a, p_b = p_b, p_a
    # assuming a - >b -> c 
    p_d = p_c[0] + (p_a[0]- p_b[0]), p_a[1] + (p_c[1] - p_b[1])
    print("{:.3f} {:.3f}".format(p_d[0], p_d[1]))
  except(EOFError):
    break
