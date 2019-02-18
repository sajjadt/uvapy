
# Corss and right hand rule can be used to figure out the relative turn (left or right)
# Idea used in Graham scan algorithm
def cross(o, a, b):
  return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

while True:
  n = int(input())
  if n == 0:
    break
    
  points = []
  for i in range(n):
    points.append(tuple(map(int, input().split())))

  # 0,1,2
  c_v = cross(points[0], points[1], points[2])
  is_convex = True

  # 
  for i in range(2, n-1):
    # turn from a[i-1] -- a[i] -- a[i+1]
    c_t = cross(points[i-1], points[i], points[i+1])
    if c_t * c_v < 0:
      is_convex = False
      break
  
  c_t = cross(points[-1], points[0], points[1])
  if c_t * c_v < 0:
    is_convex = False
  c_t = cross(points[-2], points[-1], points[0])
  if c_t * c_v < 0:
    is_convex = False


  print("No" if is_convex else "Yes")