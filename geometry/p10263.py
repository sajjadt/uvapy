def point_segment_distance(p, pa, pb):
  from math import sqrt
  A = p[0] - pa[0]
  B = p[1] - pa[1]
  C = pb[0] - pa[0]
  D = pb[1] - pa[1]

  dot = A * C + B * D
  len_sq = C * C + D * D
  param = -1
  if len_sq != 0: #in case of 0 length line
      param = dot / len_sq

  if param < 0:
    xx = pa[0]
    yy = pa[1]
  elif param > 1:
    xx = pb[0]
    yy = pb[1]
  else:
    xx = pa[0] + param * C
    yy = pa[1] + param * D

  dx = p[0] - xx
  dy = p[1] - yy
  return sqrt(dx * dx + dy * dy), [xx, yy]


while True:
  try:
    xm = float(input())
    ym = float(input())
    pm = [xm, ym]
    n = int(input())
    points = []
    for i in range(n+1):
      x = float(input())
      y = float(input())
      points.append([x, y])
    
    min_dist, min_p = min(map(lambda i: point_segment_distance(pm, points[i], points[i+1]), range(len(points) -1)))

    print("{:.4f}\n{:.4f}".format(min_p[0], min_p[1]))

  except(EOFError):
    break